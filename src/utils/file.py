import csv
import json
import shutil
from pathlib import Path
from striprtf.striprtf import rtf_to_text
from tqdm import tqdm
from typing import Dict, List, Tuple, Callable
from .text import get_unicode_string
from .utterance import split_utterances, str_to_dict


# Function to process a directory of text files.
def process_directory(
    fn: Callable,
    input_dir: Path | str,
    output_dir: Path | str,
    file_pattern: str = "*.txt",
    desc: str = "Running...",
    return_result: bool = False,
) -> Dict:
    input_dir, output_dir = Path(input_dir), Path(output_dir)
    content_results = {}
    files = list(input_dir.glob(file_pattern))
    for file_path in tqdm(files, total=len(files), desc=desc):
        content = fn(file_path=file_path)
        write_text(
            content=content,
            dest=change_file_extension(file_path=file_path, input_dir=output_dir),
        )
        if return_result:
            content_results.update(str_to_dict(content))
    return content_results


# File reading functions.
def read_tokens(file_path: Path | str) -> List[str]:
    return read_file(file_path=Path(file_path)).split()


def read_list(file_path: Path | str) -> List[str]:
    return read_file(file_path=Path(file_path)).split("\n")


def read_dict(file_path: Path) -> Dict:
    return json.loads(read_file(file_path=file_path.with_suffix(".json")))


def read_file(file_path: Path | str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


# File writing functions.
def write_text(
    content: str,
    dest: Path | str,
    exist_ok: bool = True,
    use_unicode: bool = False,
    skip_newline: bool = False,
) -> None:
    dest = Path(dest)
    if use_unicode:
        content = get_unicode_string(content, skip_newline)
        dest = dest.parent / Path(dest.stem + "_utf")
    write_file(content=content, dest=dest.with_suffix(".txt"), exist_ok=exist_ok)


def write_json(
    data: Dict,
    dest: Path | str,
    use_unicode: bool = False,
) -> None:
    dest = Path(dest)
    if use_unicode:
        json_data = json.dumps(data)
        dest = dest.parent / Path(dest.stem + "_utf")
    else:
        json_data = json.dumps(data, ensure_ascii=False)
    write_file(content=json_data, dest=dest.with_suffix(".json"))


def write_csv(data: Dict, fieldnames: Tuple, dest: Path | str) -> None:
    dest = Path(dest)
    with open(
        dest.with_suffix(".csv"), mode="w", encoding="utf-8", newline=""
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for word_bn, word_mm in data.items():
            writer.writerow({fieldnames[0]: word_bn, fieldnames[1]: word_mm})


def write_file(content: str, dest: Path | str, exist_ok: bool = True) -> None:
    Path(dest).parent.mkdir(parents=True, exist_ok=exist_ok)
    Path(dest).write_text(data=content, encoding="utf-8")


# Function to handle file name changes.
def change_file_extension(
    file_path: Path, input_dir: Path, extension: str = "txt"
) -> Path:
    return input_dir / f"{file_path.stem}.{extension}"


# Utterance Level
def get_utt_ids(file_path: Path) -> List[str]:
    utt_ids, _ = split_utterances(content=read_file(file_path=file_path))
    return utt_ids


def read_utterances(file_path: Path) -> str:
    _, utterances = split_utterances(content=read_file(file_path=file_path))
    return "\n".join(utterances)


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


# ! This will overwrite existing files, take care!!!
def create_raw_folder() -> None:
    # rtf/*.rtf -> raw/*.txt
    input_dir = Path("data/lang/rtf")
    output_dir = Path("data/lang/raw")
    files = list(input_dir.glob("*.rtf"))
    for file_path in files:
        write_text(
            content="",
            dest=change_file_extension(file_path=file_path, input_dir=output_dir),
            exist_ok=False,
        )


# ! This will overwrite existing files, take care!!!
def create_segment_folder(
    wav_files: List[Path], output_parent_dir: Path, include_file: bool = False
) -> None:
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
