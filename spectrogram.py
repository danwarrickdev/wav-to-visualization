import warnings
import numpy as np
import seaborn as sns
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import soundfile as sf
import pandas as pd

# Suppress WavFileWarning
warnings.simplefilter("ignore", category=UserWarning)


def generate_spectrogram(file_path, sample_size, channels, graph_type):
    print(graph_type)
    # Read audio file
    data = read_audio_file(file_path)
    # Get audio file data - mono/stereo, encoding, length
    parsed = coerce_channels(data, channels)
    # Determine center by highest value
    center = get_center_by_highest_amplitude(parsed)
    # Get subset to graph?
    subset = get_data_by_range(parsed, center, sample_size)
    # Graph
    graph_data(subset, graph_type)


def read_audio_file(filename):
    data, samplerate = sf.read(filename)
    return data


def coerce_channels(data, channels):
    if data.ndim == 1:
        is_mono_stereo = "mono"
        return np.stack([data, data[::-1]], axis=-1)
    else:
        is_mono_stereo = "stereo"
        if is_mono_stereo != channels:
            coerced_mono = data.mean(axis=1)
            # return as mono
            return np.stack([coerced_mono, coerced_mono[::-1]], axis=-1)
    return data


def get_center_by_highest_amplitude(data):
    largest = 0
    largest_idx = 0
    for i in range(len(data)):
        if data[i][0] > largest:
            largest = data[i][0]
            largest_idx = i
    return largest_idx


def get_data_by_range(data, center, range):
    offset = range / 2
    lower_bound = int(center - (offset / 2))
    upper_bound = int(center + (offset / 2))

    return data[lower_bound:upper_bound]


def graph_data(data, graph_type):
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    df = pd.DataFrame({"x": x, "y": y})
    sns.set_theme(style="ticks")
    sns.jointplot(
        data=df,
        x="x",
        y="y",
        # “scatter” | “kde” | “hist” | “hex” | “reg” | “resid” 
        kind=graph_type,
        color="black",
    )
    plt.show()
