import warnings
import numpy as np
import seaborn as sns
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import soundfile as sf
import pandas as pd
from scipy.io import wavfile

# Suppress WavFileWarning
warnings.simplefilter("ignore", category=UserWarning)


def get_audio_file_as_array(filename):
    samplerate, data = wavfile.read(filename)
    # # Read the audio file
    print(data)
    return data


def make_graph(amps):
    # Check if amps is 1D or 2D
    if amps.ndim == 1:
        print("Mono")
        # Mono audio
        x = amps  # Inverting the values directly
        y = np.zeros_like(x)  # Create a dummy y for plotting
    else:
        print("Stereo")
        # Stereo audio (or more channels)
        print(amps[0:10])
        amps = amps.flatten()  # Flatten to 1D if multi-dimensional
        x = []
        y = []

        ctr = 0
        for i in amps.reshape(-1, 2):  # Reshape to handle stereo
            x.append(i[0])
            y.append(i[1])
            ctr += 1

    # Create a DataFrame and handle outliers by scaling
    data = pd.DataFrame({"x": x, "y": y})
    data["x"] = min_max_scaling(data["x"])
    data["y"] = min_max_scaling(data["y"])

    # Set the Seaborn theme
    sns.set_theme(style="ticks")
    try:
        # Plot the jointplot
        sns.jointplot(
            data=data,
            x="x",
            y="y",
            kind="hex",
            color="black",
        )

    except ValueError as e:
        print("Something went wrong...")
        print(e)

    plt.show()


def get_data_subset(arr, size):
    largest = 0
    largest_idx = 0
    for i in range(len(arr)):
        if arr[i][1] > largest:
            largest = arr[i][1]
            largest_idx = i

    lower_bound = int(largest_idx - (size / 2))
    upper_bound = int(largest_idx + (size / 2))
    return arr[lower_bound:upper_bound]


def generate_spectrogram(file_path, sample_size):
    d = get_audio_file_as_array(file_path)
    s = get_data_subset(d, sample_size)
    print(s.shape)
    make_graph(s)


def min_max_scaling(data):
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)


def main():
    generate_spectrogram("assets/alien.wav", 1000)


if __name__ == "__main__":
    main()
