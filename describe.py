import os
from typing import Collection, List
from matplotlib import pyplot as plt
import pandas as pd
from src.config.paths import GEN_DIR, RAW_DATA, WAV_DATA
from src.utils.file import fget
from src.utils.project import speaker_dict, time_dict, month_dict, year_dict


def describe():
    audios = {audio.stem for audio in fget(WAV_DATA, extension="txt")}
    scripts = {script.stem for script in fget(RAW_DATA, extension="txt")}

    print_stage_status(audios, desc="audio file")
    print_stage_status(scripts, desc="script file")

    generate([script[:12] for script in scripts])


def print_stage_status(data_list: Collection[str], desc: str = "file") -> None:
    if not data_list:
        print(f"No {desc}s found.")
        return

    l1 = [data for data in data_list if 8 <= len(data) <= 9]
    l2 = [data for data in data_list if 12 <= len(data) <= 13]
    l3 = [data for data in data_list if len(data) == 16]
    l4 = [data for data in data_list if len(data) not in {8, 9, 12, 13, 16}]

    total_count = len(data_list)
    stage_counts = [len(l1), len(l2), len(l3), len(l4)]
    stage_names = [
        "stage 1 (slot)",
        "stage 2 (speaker)",
        "stage 3 (utterance)",
        "unprepared",
    ]

    print(f"Total Number of {desc}(s): {total_count}")
    for stage_name, stage_count in zip(stage_names, stage_counts):
        stage_percentage = (stage_count / total_count) * 100
        print(
            f"Number of {desc}(s) in {stage_name}: {stage_count} | {stage_percentage:.2f}%"
        )


def generate(scripts: Collection[str]) -> None:
    script_info_df = build_file_and_speaker_info(list(scripts))
    os.makedirs(GEN_DIR, exist_ok=True)
    script_info_df.to_csv(GEN_DIR / "script_info.csv", index=False)
    sorted_script_info_df = script_info_df.sort_values(by="spk_id")
    sorted_script_info_df.to_csv(GEN_DIR / "sorted_script_info.csv", index=False)
    plot_dataset_speakers(script_info_df)


def build_file_and_speaker_info(file_list: List[str]) -> pd.DataFrame:
    """
    Build a DataFrame for file IDs and speaker IDs from a list of file names using pandas DataFrame.

    Args:
        file_list (List[str]): A list of file names in the format "slot-speaker" or "slot-speaker-utterance".

    Returns:
        pd.DataFrame: A DataFrame containing columns 'file_name', 'slot', and 'spk_id'.
    """
    df = pd.DataFrame(file_list, columns=["file_name"])
    df[["slot", "spk_id"]] = df["file_name"].str.split("-", n=2, expand=True)
    df[["year", "month", "day", "time"]] = df["slot"].str.extract(
        r"(\d{2})(\d{2})(\d{2})(\d{2})"
    )
    df.drop_duplicates(inplace=True)
    df["year"] = df["year"].map(year_dict)
    df["month"] = df["month"].map(month_dict)
    df["time"] = df["time"].map(time_dict)
    df["speaker_name"] = df["spk_id"].map(speaker_dict)

    return df


def plot_dataset_speakers(file_info_df: pd.DataFrame) -> None:
    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # Adjusted to restore plot size
    fig.suptitle("Dataset Analysis - Speakers", fontsize=16)

    # Plot 1: Bar graph from spk_info
    ax1 = axes[0]
    spk_info_df = file_info_df.groupby("spk_id").size().reset_index(name="count")
    bars = ax1.bar(spk_info_df["spk_id"], spk_info_df["count"])
    ax1.set_title("Speaker Counts")
    ax1.set_xlabel("Speaker ID")
    ax1.set_ylabel("Count")

    # Add labels with counts on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset for better positioning
            textcoords="offset points",
            ha="center",
            va="bottom",
        )

    # Plot 2: Pie chart from spk_info
    ax2 = axes[1]

    # Uncomment this if speaker name is preferred
    # spk_info_df_2 = file_info_df.groupby("speaker_name").size().reset_index(name="")
    # spk_info_df_2.set_index("speaker_name").plot(
    #     kind="pie", y="", autopct="%1.1f%%", legend=False, startangle=90, ax=ax2
    # )
    spk_info_df = file_info_df.groupby("spk_id").size().reset_index(name="")
    spk_info_df.set_index("spk_id").plot(
        kind="pie", y="", autopct="%1.1f%%", legend=False, startangle=90, ax=ax2
    )
    ax2.set_title("Speaker Distribution")
    ax2.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle

    # Save each subplot to a file
    fig.savefig(
        (GEN_DIR / "speaker_distribution_plot.png").as_posix(), bbox_inches="tight"
    )

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust subplot layout
    plt.show()


if __name__ == "__main__":
    describe()
