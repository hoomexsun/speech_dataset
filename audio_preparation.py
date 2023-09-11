from src.config.paths import SEG_DATA, WAV_DATA
from src.utils.file import create_segment_folder


def prepare_audio():
    wav_files = list(WAV_DATA.glob("*.wav"))
    create_segment_folder(
        wav_files=wav_files, output_parent_dir=SEG_DATA, include_file=True
    )


if __name__ == "__main__":
    prepare_audio()
