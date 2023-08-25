from typing import Collection, Dict, List, Set, Tuple
from config.paths import *
from utils.file import get_dict_from_json
from config.position import BEGIN, END, MID
from config.syllabic import CODA, ONSET, NUCLEUS
from utils.text import pct, remove_chars


class Clusters:
    bn_cmap = {}
    mm_m2l = {}

    def __new__(cls):
        cls.__init_res()
        return super().__new__(cls)

    @classmethod
    def __init_res(cls):
        bn_to_mm_charmap = get_dict_from_json(file_path=TRANSLITERATION_DIR / B2M_FILE)
        mm_charmap = get_dict_from_json(file_path=ALPHABET_DIR / MM_ALPHABET_FILE)
        cls.bn_cmap = bn_to_mm_charmap.get("bn_single_charmap", {})
        cls.bn_viramma_mm_apun = bn_to_mm_charmap.get("bn_viramma_mm_apun", {})
        cls.bn_viramma_mm_coda = bn_to_mm_charmap.get("bn_viramma_mm_coda", {})
        cls.mm_e_lonsum_coda = bn_to_mm_charmap.get("mm_e_lonsum_coda", {})
        cls.mm_m2l = bn_to_mm_charmap.get("mm_mapum_to_lonsum", {})
        cls.mm_lonsum_to_mapum = bn_to_mm_charmap.get("mm_lonsum_to_mapum", {})
        cls.mm_chars = mm_charmap.get("mm_chars", [])
        cls.mm_mapum = mm_charmap.get("mm_mapum", [])
        cls.mm_lonsum = mm_charmap.get("mm_lonsum", [])
        cls.mm_cheitap = mm_charmap.get("mm_cheitap", [])
        cls.mm_cheising = mm_charmap.get("mm_cheising", [])
        cls.mm_khudam = mm_charmap.get("mm_khudam", [])

    @staticmethod
    def get_clusters(content: str) -> Set:
        virama = "\u09cd"
        chars_to_remove = [",", "-", "-", ".", "(", ")"]
        content = remove_chars(content=content, chars=chars_to_remove)
        clusters = set()
        i = 0
        while i < len(content):
            skip = 1
            if content[i] == virama:
                cluster = content[i - 1 : i + 2]
                if i + 3 < len(content) and content[i + 2] == virama:
                    cluster += content[i + 2 : i + 4]
                    skip += 2
                skip += 2
                clusters.add(cluster)
            i += skip
        return clusters

    @staticmethod
    def build_egs(content: str, clusters: Collection) -> Dict[str, List]:
        cluster_egs = {cluster: [] for cluster in clusters}
        for cluster in clusters:
            for word in set(content.split()):
                if cluster in word and word not in cluster_egs[cluster]:
                    cluster_egs[cluster].append(word)
        return cluster_egs

    @staticmethod
    def build_probable_map(clusters: Collection) -> Dict[str, Dict[str, str]]:
        maps = {}
        for cluster in clusters:
            maps[cluster] = {
                str(BEGIN): Clusters.get_mm_cluster(cluster=cluster, pos=BEGIN),
                str(MID): Clusters.get_mm_cluster(cluster=cluster, pos=MID),
                str(END): Clusters.get_mm_cluster(cluster=cluster, pos=END),
            }
        return maps

    @classmethod
    def build_detailed_clusters(
        cls, cluster_egs, total_words: int
    ) -> Tuple[Dict, Dict]:
        detailed_clusters, clusters_pct = {}, {}
        mp, ct, egs_key = "map", "count", "egs"
        num_clusters = len(cluster_egs)
        for cluster, egs in cluster_egs.items():
            b_egs, m_egs, e_egs = [], [], []
            for eg in egs:
                pos = cls.get_pos_of_cluster(cluster, eg)
                if pos == BEGIN:
                    # b_egs.append([eg, self.get_mm_cluster(cluster, BEGIN, eg)])
                    b_egs.append(eg)
                elif pos == END:
                    # e_egs.append([eg, self.get_mm_cluster(cluster, END, eg)])
                    e_egs.append(eg)
                elif pos == MID:
                    # m_egs.append([eg, self.get_mm_cluster(cluster, MID, eg)])
                    m_egs.append(eg)
            detailed_clusters[cluster] = {
                BEGIN: {
                    mp: cls.get_mm_cluster(cluster, BEGIN),
                    egs_key: b_egs,
                    ct: len(b_egs),
                },
                MID: {
                    mp: cls.get_mm_cluster(cluster, MID),
                    egs_key: m_egs,
                    ct: len(m_egs),
                },
                END: {
                    mp: cls.get_mm_cluster(cluster, END),
                    egs_key: e_egs,
                    ct: len(e_egs),
                },
            }

            clusters_pct[cluster] = {
                BEGIN: {
                    mp: cls.get_mm_cluster(cluster, BEGIN),
                    ct: len(b_egs),
                    "pct": pct(len(b_egs), num_clusters),
                },
                MID: {
                    mp: cls.get_mm_cluster(cluster, MID),
                    ct: len(m_egs),
                    "pct": pct(len(m_egs), num_clusters),
                },
                END: {
                    mp: cls.get_mm_cluster(cluster, END),
                    ct: len(e_egs),
                    "pct": pct(len(e_egs), num_clusters),
                },
                ct: len(egs),
                "pct": pct(len(egs), total_words),
            }
        return detailed_clusters, clusters_pct

    # Get position of Cluster
    @staticmethod
    def get_pos_of_cluster(cluster, word) -> str | None:
        if word.startswith(cluster):
            return BEGIN
        elif word.endswith(cluster):
            return END
        elif cluster in word:
            return MID

    @classmethod
    def get_mm_cluster(cls, cluster: str, pos: str, word: str = "") -> str:
        c1, c2, c3 = cluster[0], cluster[2], "" if len(cluster) == 3 else cluster[4]
        t1, t2, t3 = "", "", ""
        idx = word.find(cluster)
        if c3 and c3 == "র" and (pos == END or pos == MID):
            t1, t2, t3 = CODA, ONSET, ONSET
        elif c3 and c1 == "র" and (pos == END or pos == MID):
            t1, t2, t3 = CODA, CODA, CODA
        elif c3 and (pos == END or pos == MID):
            t1, t2, t3 = CODA, ONSET, ONSET
        elif c3 and pos == BEGIN:
            t1, t2, t3 = ONSET, ONSET, ONSET
        elif c2 == "য" or c2 == "র":
            t1, t2 = ONSET, ONSET
        elif c2 == "ব":
            c2 = "ꯋ"
            t1, t2 = ONSET, ONSET

        else:
            t1, t2 = CODA, ONSET

        apun, c = "\uabed", ""
        temp = cls.bn_cmap.get(c1, c1)
        c = cls.mm_m2l.get(temp, temp) if t1 == CODA else f"{temp}{apun}"
        temp = cls.bn_cmap.get(c2, c2)
        c += cls.mm_m2l.get(temp, temp) if t2 == CODA else temp
        if c3:
            temp = cls.bn_cmap.get(c3, c3)
            c += cls.mm_m2l.get(temp, temp) if t3 == CODA else f"{apun}{temp}"

        return c
