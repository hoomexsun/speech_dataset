from config.log import setup_logger
from pathlib import Path
from pydub import AudioSegment
import shutil
from typing import List
from tqdm import tqdm


def mp3_to_wav(mp3_files: List[Path]) -> None:
    logger = setup_logger("logs/mp3_3_wav.log")
    logger.info(f"Converting {len(mp3_files)} MP3 files to WAV files.")
    for idx, mp3_file in enumerate(
        tqdm(mp3_files, total=len(mp3_files), desc="Converting MP3 files to WAV files")
    ):
        if not mp3_file.exists():
            raise FileNotFoundError(f"File not found: {mp3_file=}")
        wav_file = mp3_file.parent / (mp3_file.stem + ".wav")
        sound = AudioSegment.from_mp3(str(mp3_file))
        sound.export(str(wav_file), format="wav")
        logger.info(f"Converted: {mp3_file} to {wav_file} ({idx+1}/{len(mp3_files)})")


def stereo_to_mono(stereo_wav_files: List[Path]) -> None:
    converted, not_converted = 0, 0
    logger = setup_logger("logs/stereo_wav_to_mono.log")
    logger.info(
        f"Started converting {len(stereo_wav_files)} stereo WAV files to mono using Pydub"
    )

    for idx, stereo_wav_file in enumerate(
        tqdm(
            stereo_wav_files,
            total=len(stereo_wav_files),
            desc="Converting stereo WAV files to mono",
        )
    ):
        if not stereo_wav_file.exists():
            raise FileNotFoundError(f"{stereo_wav_file=} does not exist.")
        elif is_dual_channel_wav(stereo_wav_file):
            mono_file = stereo_wav_file.parent / (stereo_wav_file.stem + ".wav")
            sound = AudioSegment.from_wav(str(stereo_wav_file))
            sound.set_channels(1)
            sound.export(mono_file, format="wav")
            converted += 1
            logger.info(
                f"Converted: {stereo_wav_file} to mono ({idx+1}/{len(stereo_wav_files)})"
            )
        else:
            not_converted += 1
            logger.info(
                f"Not Converted: {stereo_wav_file} (Already mono) ({idx+1}/{len(stereo_wav_files)})"
            )
        logger.info(
            f"Converted {converted} files to mono | Not converted {not_converted} files (already mono)"
        )


def is_dual_channel_wav(file_path: Path) -> bool:
    wav_file = AudioSegment.from_wav(file_path)
    return wav_file.channels == 2
