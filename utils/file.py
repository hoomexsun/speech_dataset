from pathlib import Path
import shutil
from striprtf.striprtf import rtf_to_text
from typing import Dict, List, Tuple
import json
import csv
from tqdm import tqdm
from config.paths import RAW_DATA, RTF_DATA
from utils.text import get_unicode_string


def get_files(dir: Path, extension: str = "txt") -> List[Path]:
    return list(dir.glob(f"*.{extension.lower()}"))


def get_dict_from_json(file_path: Path) -> Dict:
    """Load data from a JSON file and return it as a dictionary.

    Args:
        file_path (Path): Path to the JSON file.

    Returns:
        Dict: Loaded data as a dictionary.
    """
    json_data = read_encoded_file(file_path=file_path.with_suffix(".json"))
    return json.loads(json_data)


def get_text_from_rtf(file_path: Path) -> str:
    """Extract plain text from an RTF file.

    Args:
        file_path (Path): Path to the RTF file.

    Returns:
        str: Plain text extracted from the RTF file.
    """
    with open(file_path, "rb") as rtf_file:
        rtf_data = rtf_file.read()
        try:
            rtf_text = rtf_data.decode("utf-8")
        except UnicodeDecodeError:
            try:
                rtf_text = rtf_data.decode("cp1252")
            except UnicodeDecodeError:
                rtf_text = rtf_data.decode("utf-8", errors="replace")

        if isinstance(rtf_text, str):
            plain_text = rtf_to_text(rtf_text)
        else:
            raise ValueError("Unable to extract text from the RTF file.")
        plain_text = plain_text.replace("\x00", "").replace("\xdd", "")

    return plain_text


def modify_unicode_file_path(file_path: Path) -> Path:
    file_name = file_path.stem + "_utf"
    return file_path.parent / file_name


def write_text_file(
    content: str,
    file_path: Path,
    exist_ok: bool = True,
    unicode: bool = False,
    skip_newline: bool = False,
) -> None:
    if unicode:
        content = get_unicode_string(content, skip_newline)
        file_path = modify_unicode_file_path(file_path)
    write_encoded_file(
        content=content, file_path=file_path.with_suffix(".txt"), exist_ok=exist_ok
    )


def write_markdown_file(content: str, file_path: Path) -> None:
    write_encoded_file(content=content, file_path=file_path.with_suffix(".md"))


def write_json_file(data: Dict, file_path: Path, unicode: bool = False) -> None:
    if unicode:
        json_data = json.dumps(data)
        file_path = modify_unicode_file_path(file_path)
    else:
        json_data = json.dumps(data, ensure_ascii=False)
    write_encoded_file(content=json_data, file_path=file_path.with_suffix(".json"))


def write_csv_file(data: Dict, fieldnames: Tuple, file_path: Path) -> None:
    file_path = file_path.with_suffix(".csv")
    with open(file_path, mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for word_bn, word_mm in data.items():
            writer.writerow({fieldnames[0]: word_bn, fieldnames[1]: word_mm})


def read_encoded_file(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def write_encoded_file(content: str, file_path: Path, exist_ok: bool = True) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=exist_ok)
    file_path.write_text(data=content, encoding="utf-8")


# Path Modifier
def change_path(file_path: Path, dir: Path, extension: str = "txt"):
    return dir / f"{file_path.stem}.{extension}"


# Audio File
# ! This will overwrite existing files, take care!!!
def create_segment_folder(
    wav_files: List[Path], output_parent_dir: Path, include_file: bool = False
):
    paths = [output_parent_dir / path.stem for path in wav_files]
    total_files = len(wav_files)

    if not include_file:
        with tqdm(
            total=total_files, desc=f"Creating Folders ({total_files} files)"
        ) as pbar:
            for path in paths:
                path.mkdir(parents=True, exist_ok=False)
                pbar.update(1)
    else:
        with tqdm(
            total=total_files, desc=f"Copying Files ({total_files} files)"
        ) as pbar:
            for original_file, destination_path in zip(wav_files, paths):
                destination_path.mkdir(parents=True, exist_ok=True)
                shutil.copy(original_file, destination_path / original_file.name)
                pbar.update(1)

    print(f"Created folders for segmented wav files ({total_files} files)")


# Text File
# ! This will overwrite existing files, take care!!!
@staticmethod
def create_raw_folder():
    files = get_files(dir=RTF_DATA, extension="rtf")
    for file_path in files:
        write_text_file(
            content="",
            file_path=change_path(file_path=file_path, dir=RAW_DATA),
            exist_ok=False,
        )


# Utterance Utility Functions
def build_utt_id(file_path: Path, idx: int) -> str:
    utt_id = file_path.name.split(".")[0]
    if idx < 9:  # idx starts from 0
        utt_id = f"{utt_id}00{idx+1}"
    elif idx < 99:
        utt_id = f"{utt_id}0{idx+1}"
    else:
        utt_id = f"{utt_id}{idx+1}"
    return utt_id


def get_utt_ids_from_text(file_path: Path) -> List[str]:
    utt_ids, _ = split_id_and_utt(file_path=file_path)
    return utt_ids


def get_utterances_from_text(file_path: Path) -> str:
    _, utterances = split_id_and_utt(file_path=file_path)
    return "\n".join(utterances)


def split_id_and_utt(file_path: Path) -> Tuple[List, List]:
    temp = read_encoded_file(file_path=file_path)
    lines = temp.split("\n")
    utt_ids, utterances = [], []
    for line in lines:
        utt_id, *utterance = line.split("\t")
        utt_ids.append(utt_id)
        utterances.extend(utterance)
    return utt_ids, utterances
