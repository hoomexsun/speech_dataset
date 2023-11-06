from typing import Dict, List, Tuple


# File Level Utternace related operations
def utt_id(file_name: str, idx: int) -> str:
    if idx < 9:  # idx starts from 0
        return f"{file_name}00{idx+1}"
    elif idx < 99:
        return f"{file_name}0{idx+1}"
    else:
        return f"{file_name}{idx+1}"


# String Level Utterance related operations
def dict_to_str(utterances_dict: Dict[str, str]) -> str:
    return "\n".join(f"{utt_id}\t{utt}" for utt_id, utt in utterances_dict.items())


def str_to_dict(content: str) -> Dict[str, str]:
    if not content:
        return {}
    lines = content.split("\n")
    utt_ids, utterances = [], []
    for line in lines:
        utt_id, *utterance = line.split("\t")
        utt_ids.append(utt_id)
        utterances.extend(utterance)
    return list_to_dict(utt_ids, utterances)


def list_to_dict(utt_ids: List[str], utterances: List[str]) -> Dict[str, str]:
    return {utt_id: utt for utt_id, utt in zip(utt_ids, utterances)}


def list_to_str(utt_ids: List[str], utterances: List[str]) -> str:
    return "".join(f"{utt_id}\t{utt}\n" for utt_id, utt in zip(utt_ids, utterances))


def split_utterances(content: str) -> Tuple[List, List]:
    lines = content.split("\n")
    utt_ids, utterances = [], []
    for line in lines:
        utt_id, *utterance = line.split("\t")
        utt_ids.append(utt_id)
        utterances.extend(utterance)
    return utt_ids, utterances
