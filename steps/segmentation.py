from pathlib import Path
import shutil
from typing import List
from tqdm import tqdm


def create_segmentation_folders(
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


# Example usage:
# wav_files = [Path("file1.wav"), Path("file2.wav"), ...]
# output_parent_dir = Path("output_directory")
# create_segmentation_folders(wav_files, output_parent_dir, include_file=True)
