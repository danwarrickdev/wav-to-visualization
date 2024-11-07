### Description

This project was made for an artist client who was looking to convert a sound file (.wav) into a visualization in such a way they could use the resulting png to create 3d printer instructions and ultimates create a sculpture representative of a specific sound.

Running the script opens a UI made with tKinter that allows uploading a .wav file and uses Seaborn to output a visualization of that audio file.

### Getting started

##### Python3

```
# clone repo with ssh
git clone git@github.com:danwarrickdev/wav-to-visualization.git

# cd into project
cd wav-to-visualization

# install deps
pip install -r requirements.txt

# run project
python index.py
```

### PyInstaller

I built this to be easy to ship as an executable so the client doesn't need to worry about terminal interactions

```
# cd into project
cd wav-to-visualization

# create executable
pyinstaller --onefile index.py
```
