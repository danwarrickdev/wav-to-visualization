import numpy as np
import pandas as pd
import seaborn as sns
import soundfile as sf
import matplotlib.pyplot as plt

def plot_audio_with_jointplot(filename):
    # Read the audio file
    data, samplerate = sf.read(filename)

    # Create a time array in seconds
    if data.ndim == 1:
        time = np.linspace(0, len(data) / samplerate, num=len(data))
        amplitude = data
    elif data.ndim == 2:
        time = np.linspace(0, len(data) / samplerate, num=len(data))
        amplitude = data.mean(axis=1)  # Average both channels for plotting
    else:
        print("Unsupported number of channels.")
        return

    # Remove leading and trailing zeros from amplitude
    non_zero_indices = np.where(amplitude != 0)[0]
    
    if non_zero_indices.size > 0:
        first_non_zero = non_zero_indices[0]
        last_non_zero = non_zero_indices[-1]
        
        trimmed_time = time[first_non_zero:last_non_zero + 1]
        trimmed_amplitude = amplitude[first_non_zero:last_non_zero + 1]
    else:
        print("No non-zero amplitudes found.")
        return

    # Create a DataFrame for Seaborn
    df = pd.DataFrame({'Time (s)': trimmed_time, 'Amplitude': trimmed_amplitude})

    # Plotting with Seaborn jointplot
    sns.set_theme(style="ticks")
    joint_plot = sns.jointplot(data=df, x='Time (s)', y='Amplitude', kind='hex', cmap='Blues',gridsize=30)
    joint_plot.ax_joint.set_title("Audio Waveform")
    joint_plot.ax_joint.set_xlabel("Time (seconds)")
    joint_plot.ax_joint.set_ylabel("Amplitude")

    plt.show()

