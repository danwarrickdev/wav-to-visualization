from tkinter import *
from tkinter import filedialog
from spectrogram import generate_spectrogram


def handle_upload_file(root, sample_size, channels):
    root.filename = filedialog.askopenfilename(
        initialdir="/Users", title="Select a file", filetypes=[("wav files", "*.wav")]
    )
    file_label = Label(root, text=root.filename.split("/")[-1])
    file_label.pack()
    generate_spectrogram(root.filename, int(sample_size), channels)


def main():
    root = Tk()
    root.title("Spectrogram Generator")
    root.geometry("400x400")
    title = Label(root, text="Audio to Spectrogram", pady=25)
    desc = Label(
        root, text="A program to visualize .wav files as spectrograms", pady=25
    )
    
    # Create a variable to store the selected value
    channels = StringVar(value="mono")

    # Create the radio buttons
    radio1 = Radiobutton(root, text="Mono", variable=channels, value="mono")
    radio2 = Radiobutton(root, text="Stereo", variable=channels, value="stereo")

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
        command=lambda: handle_upload_file(root, input_size.get(), channels.get()),
    )

    for i in [
        title,
        desc,
        radio1,
        radio2,
        input_size_container,
        input_size,
        upload_btn,
    ]:
        i.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
