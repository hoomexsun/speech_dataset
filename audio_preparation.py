from config.paths import *
from steps.segmentation import create_segmentation_folders


def prepare_audio():
    wav_files = list(WAV_DATA.glob("*.wav"))
    create_segmentation_folders(
        wav_files=wav_files, output_parent_dir=SEG_DATA, include_file=True
    )


if __name__ == "__main__":
    prepare_audio()
