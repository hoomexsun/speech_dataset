from pathlib import Path
from pydub import AudioSegment
from typing import List
from tqdm import tqdm


def mp3_to_wav(mp3_files: List[Path]) -> None:
    for mp3_file in tqdm(
        mp3_files, total=len(mp3_files), desc="Converting MP3 files to WAV files"
    ):
        if not mp3_file.exists():
            raise FileNotFoundError(f"File not found: {mp3_file=}")
        wav_file = mp3_file.parent / (mp3_file.stem + ".wav")
        sound = AudioSegment.from_mp3(str(mp3_file))
        sound.export(str(wav_file), format="wav")


def stereo_to_mono(stereo_wav_files: List[Path]) -> None:
    for stereo_wav_file in tqdm(
        stereo_wav_files,
        total=len(stereo_wav_files),
        desc="Converting stereo WAV files to mono",
    ):
        if not stereo_wav_file.exists():
            raise FileNotFoundError(f"{stereo_wav_file=} does not exist.")
        elif is_dual_channel_wav(stereo_wav_file):
            mono_file = stereo_wav_file.parent / (stereo_wav_file.stem + ".wav")
            sound = AudioSegment.from_wav(str(stereo_wav_file))
            sound.set_channels(1)
            sound.export(mono_file, format="wav")


def is_dual_channel_wav(file_path: Path) -> bool:
    wav_file = AudioSegment.from_wav(file_path)
    return wav_file.channels == 2
