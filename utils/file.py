from pathlib import Path
import shutil
from striprtf.striprtf import rtf_to_text
from typing import Dict, List, Tuple
import json
import csv
from tqdm import tqdm
from config.paths import RAW_DATA, RTF_DATA
from utils.text import get_unicode_string, split_id_and_utt


def fget(dir: Path, extension: str = "txt") -> List[Path]:
    return list(dir.glob(f"*.{extension.lower()}"))


def fpath_unicode(file_path: Path) -> Path:
    file_name = file_path.stem + "_utf"
    return file_path.parent / file_name


def change_path(file_path: Path, dir: Path, extension: str = "txt") -> Path:
    return dir / f"{file_path.stem}.{extension}"


def fget_items(file_path: Path) -> Dict | List[str]:
    if file_path.suffix.lower() == ".json":
        return fget_dict(file_path)
    else:
        return fget_list(file_path)


def fget_dict(file_path: Path) -> Dict:
    return json.loads(fread(file_path=file_path.with_suffix(".json")))


def fget_list(file_path: Path) -> List[str]:
    return fread(file_path=file_path).split("\n")


#! EXPERIMENTAL
def fget_rtf_text(file_path: Path) -> str:
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


def fread(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def fwrite_text(
    content: str,
    file_path: Path,
    exist_ok: bool = True,
    unicode: bool = False,
    skip_newline: bool = False,
) -> None:
    if unicode:
        content = get_unicode_string(content, skip_newline)
        file_path = fpath_unicode(file_path)
    fwrite(content=content, file_path=file_path.with_suffix(".txt"), exist_ok=exist_ok)


def fwrite_md(content: str, file_path: Path) -> None:
    fwrite(content=content, file_path=file_path.with_suffix(".md"))


def fwrite_json(data: Dict, file_path: Path, unicode: bool = False) -> None:
    if unicode:
        json_data = json.dumps(data)
        file_path = fpath_unicode(file_path)
    else:
        json_data = json.dumps(data, ensure_ascii=False)
    fwrite(content=json_data, file_path=file_path.with_suffix(".json"))


def fwrite_csv(data: Dict, fieldnames: Tuple, file_path: Path) -> None:
    with open(
        file_path.with_suffix(".csv"), mode="w", encoding="utf-8", newline=""
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for word_bn, word_mm in data.items():
            writer.writerow({fieldnames[0]: word_bn, fieldnames[1]: word_mm})


def fwrite(content: str, file_path: Path, exist_ok: bool = True) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=exist_ok)
    file_path.write_text(data=content, encoding="utf-8")


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
    files = fget(dir=RTF_DATA, extension="rtf")
    for file_path in files:
        fwrite_text(
            content="",
            file_path=change_path(file_path=file_path, dir=RAW_DATA),
            exist_ok=False,
        )


# Utterance Utility Functions
def fbuild_id(file_path: Path, idx: int) -> str:
    utt_id = file_path.name.split(".")[0]
    if idx < 9:  # idx starts from 0
        utt_id = f"{utt_id}00{idx+1}"
    elif idx < 99:
        utt_id = f"{utt_id}0{idx+1}"
    else:
        utt_id = f"{utt_id}{idx+1}"
    return utt_id


def fget_ids(file_path: Path) -> List[str]:
    utt_ids, _ = split_id_and_utt(content=fread(file_path=file_path))
    return utt_ids


def fget_utterances(file_path: Path) -> str:
    _, utterances = split_id_and_utt(content=fread(file_path=file_path))
    return "\n".join(utterances)
