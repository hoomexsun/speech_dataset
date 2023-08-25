from typing import List, Dict, Tuple


def parse_file_info(file_name: str) -> Dict[str, str]:
    """
    Parse a single file name and return a dictionary containing slot and speaker ID.

    Args:
        file_name (str): A file name in the format "slot-speaker" or "slot-speaker-utterance".

    Returns:
        Dict[str, str]: A dictionary containing "slot" and "spk_id" keys.
    """
    parts = file_name.split("-")

    if len(parts) not in {2, 3}:
        raise ValueError("Invalid file name format")

    slot, spk_id = parts[:2]

    return {"slot": slot, "spk_id": spk_id}


def build_file_and_speaker_info(
    file_list: List[str],
) -> Tuple[Dict[str, Dict[str, str]], Dict[str, Dict[str, List[str]]]]:
    """
    Build dictionaries for file IDs and speaker IDs from a list of file names.

    Args:
        file_list (List[str]): A list of file names in the format "slot-speaker" or "slot-speaker-utterance".

    Returns:
        Tuple[Dict[str, Dict[str, str]], Dict[str, Dict[str, List[str]]]]:
            - A dictionary containing file IDs mapped to slot and speaker ID.
            - A dictionary containing speaker IDs mapped to the count and a list of associated slots.
    """
    file_id_to_info = {}
    spk_id_to_info = {}

    for file_name in file_list:
        file_info = parse_file_info(file_name)
        file_id = f"{file_info['slot']}-{file_info['spk_id']}"

        # Populate file_id_to_info dictionary
        if file_id not in file_id_to_info:
            file_id_to_info[file_id] = file_info

        # Populate spk_id_to_info dictionary
        if file_info["spk_id"] not in spk_id_to_info:
            spk_id_to_info[file_info["spk_id"]] = {
                "count": 1,
                "files": [file_info["slot"]],
            }
        else:
            spk_id_to_info[file_info["spk_id"]]["count"] += 1
            spk_id_to_info[file_info["spk_id"]]["files"].append(file_info["slot"])

    return file_id_to_info, spk_id_to_info


# Example usage:
file_list = ["123456-123", "456789-456", "789101-123", "121314-456"]
file_info, spk_info = build_file_and_speaker_info(file_list)
print("File list:")
print(file_list)
print("File ID Info:")
print(file_info)
print("\nSpeaker ID Info:")
print(spk_info)
