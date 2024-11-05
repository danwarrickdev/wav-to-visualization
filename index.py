from tkinter import *
from tkinter import filedialog
from spectrogram import generate_spectrogram


def handle_upload_file(root, sample_size, channels, graph_type):
    root.filename = filedialog.askopenfilename(
        initialdir="/Users", title="Select a file", filetypes=[("wav files", "*.wav")]
    )
    file_label = Label(root, text=root.filename.split("/")[-1])
    file_label.pack()
    generate_spectrogram(root.filename, int(sample_size), channels, graph_type)


def main():
    root = Tk()
    root.title("Spectrogram Generator")
    root.geometry("640x640")
    title = Label(root, text="Audio to Spectrogram", pady=25)
    desc = Label(
        root, text="A program to visualize .wav files as spectrograms", pady=25
    )
    lbl_channel = Label(
        root, text="Channels", pady=5
    )
    # Create a variable to store the selected value
    channels = StringVar(value="mono")

    # Create the radio buttons
    rd_mono = Radiobutton(root, text="Mono", variable=channels, value="mono")
    rd_stereo = Radiobutton(root, text="Stereo", variable=channels, value="stereo")
    
    lbl_graph_type = Label(
        root, text="Graph Type", pady=5
    )
    # Create a variable to store the selected value
    graph_type = StringVar(value="hex")

    # Create the radio buttons
    rd_hex = Radiobutton(root, text="Hex", variable=graph_type, value="hex")
    rd_kde = Radiobutton(root, text="KDE", variable=graph_type, value="kde")

    input_size_container = LabelFrame(
        root, text="Data Sample Size (integer)", padx=15, pady=25
    )
    input_size = Entry(
        input_size_container,
    )
    input_size.insert(0, "1000")

    upload_btn = Button(
        root,
        text="Upload File",
        command=lambda: handle_upload_file(root, input_size.get(), channels.get(), graph_type.get()),
    )

    for i in [
        title,
        desc,
        lbl_channel,
        rd_mono,
        rd_stereo,
        lbl_graph_type,
        rd_hex,
        rd_kde,
        input_size_container,
        input_size,
        upload_btn,
    ]:
        i.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
