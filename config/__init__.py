from pathlib import Path
from enum import Enum


#! Constants
class Language(Enum):
    S550 = "s550"
    BN = "bn"
    MM = "mm"


# Position
BEGIN = "begin"
MID = "mid"
END = "end"

# Syllabic
ONSET = "onset"
NUCLEUS = "nucleus"
CODA = "coda"

#! Paths
DATA_ROOT = Path("data")
DUMP_DIR = DATA_ROOT / "dump"
LANG_DIR = DATA_ROOT / "lang"
RES_DIR = DATA_ROOT / "res"  # Root directory for resource
GEN_DIR = DATA_ROOT / "gen"
OUT_DIR = DATA_ROOT / "out"

RTF, RAW, WAV, SEG = "rtf", "raw", "wav", "seg"
NEWS, UTT, TXT, WORDS, CHARS = "news", "utt", "text", "words", "chars"

RTF_DATA = LANG_DIR / RTF  # Directory for s550 rtf file (file level)
RAW_DATA = LANG_DIR / RAW  # Directory for s550 rtf file (file level)
S550_DATA = LANG_DIR / Language.S550.value
BN_DATA = LANG_DIR / Language.BN.value
MM_DATA = LANG_DIR / Language.MM.value
WAV_DATA = LANG_DIR / WAV  # Directory for audio files
SEG_DATA = LANG_DIR / SEG  # Directory for segmented audio files

NEWS_S550_DIR = S550_DATA / NEWS  # Directory for preprocessed scripts in s550
NEWS_BN_DIR = BN_DATA / NEWS  # Directory for preprocessed scripts in Bengali
NEWS_MM_DIR = MM_DATA / NEWS  # Directory for preprocessed scripts in Meetei Mayek
UTT_S550_DIR = S550_DATA / UTT  # Directory for utterance in s550
UTT_BN_DIR = BN_DATA / UTT  # Directory for utterance in Bengali Unicode
UTT_MM_DIR = MM_DATA / UTT  # Directory for utterance in Meetei Mayek Unicode

lang_dirs = [
    NEWS_S550_DIR,
    NEWS_BN_DIR,
    NEWS_MM_DIR,
    UTT_S550_DIR,
    UTT_BN_DIR,
    UTT_MM_DIR,
    RTF_DATA,
    RAW_DATA,
    WAV_DATA,
    SEG_DATA,
]

ALPHABET_DIR = RES_DIR / "alphabet"  # Alphabet Resources
TRANSLITERATION_DIR = RES_DIR / "transliteration"  # Transliteration Resources
INFO_DIR = RES_DIR / "info"  # Resource directory for Informative resource files
CORRECTION_DIR = RES_DIR / "correction"  # Correction Resources
WORD_MAP_DIR = RES_DIR / "word_map"  # WordMap Resources

res_dirs = [
    ALPHABET_DIR,
    CORRECTION_DIR,
    TRANSLITERATION_DIR,
    INFO_DIR,
    WORD_MAP_DIR,
]


# -------------------------------- FILE NAME -------------------------------- #

WORDS_FILE = "words.txt"
CHARS_FILE = "chars.txt"
TEXT_FILE = "text.txt"

WORDS_S550_FILE = S550_DATA / WORDS / WORDS_FILE
WORDS_BN_FILE = BN_DATA / WORDS / WORDS_FILE
WORDS_MM_FILE = MM_DATA / WORDS / WORDS_FILE
CHARS_S550_FILE = S550_DATA / CHARS / CHARS_FILE
CHARS_BN_FILE = BN_DATA / CHARS / CHARS_FILE
CHARS_MM_FILE = MM_DATA / CHARS / CHARS_FILE
TEXT_S550_FILE = S550_DATA / TXT / TEXT_FILE
TEXT_BN_FILE = BN_DATA / TXT / TEXT_FILE
TEXT_MM_FILE = MM_DATA / TXT / TEXT_FILE

B2M_FILE = "b2m"  # Bengali to Meetei Mayek Character Map filename
SNB_FILE = "s2b"  # Contains s550 and Bengali characters which should be mapped
FPOS_FILE = (
    "fpos"  # Contains Dictionary of List of characters which position needs fixing
)

CLUSTERS_FILE = INFO_DIR / "clusters"  # virama clusters file
CLUSTERS_EGS_FILE = INFO_DIR / "clusters_egs"  # clusters file with examples
CLUSTERS_MAP_FILE = INFO_DIR / "clusters_map"  # clusters file with probable map
CLUSTERS_DETAILED_FILE = INFO_DIR / "clusters_detailed"  # detailed clusters file
CLUSTERS_PCT_FILE = INFO_DIR / "clusters_percentage"  # detailed clusters file

WORDMAP_C_FILE = WORD_MAP_DIR / "s550_bn"
WORDMAP_T_FILE = WORD_MAP_DIR / "bn_mm"

MM_ALPHABET_FILE = (
    ALPHABET_DIR / "mm_alphabet"
)  # Contains Dictionary of List of Meetei Mayek Characters

BN_ALPHABET_FILE = (
    ALPHABET_DIR / "bn_alphabet"
)  # Contains Dictionary of List of Bengali Characters
EN_ALPHABET_FILE = (
    ALPHABET_DIR / "en_alphabet"
)  # Contains Dictionary of List of English Characters

# -------------------------------- COLUMN NAME -------------------------------- #

BN_FIELD = "bengali"  # Column name of Bengali words in WordMap file
MM_FIELD = "meetei_mayek"  # Column name of Meetei Mayek words in WordMap file


speaker_dict = {
    "001": "RK Gorani",
    "002": "Maibam Dwijamani",
    "003": "Ngangbam Nganthoi",
    "004": "Ngangom Kiran",
    "005": "Nayeni Devi",
    "006": "Wahengbam Rajesh",
    "007": "Nolini Devi",
    "008": "Wahengbam Washington",
    "009": "Kshetrimayum Chitrabhanu",
    "011": "Ningthoukhongjam Suni",
    "013": "Moirangthem Ibeyaibi",
}
month_dict = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}
time_dict = {"00": "0730", "01": "1200", "02": "1930"}
year_dict = {"20": "2020", "21": "2021"}
