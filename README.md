# InventarieSystem

## About
This application is made to keep track off the borrowed furniture and other things that needs to be tracked. This program was made for [LARV](https://larv.org/), and is created to organize furniture for the fair. This program was build for LARV 2022.

To use the program the .exe file will need 2 files to work:
* logga-fyrkant.png
* logo_icon.png

## Dependencies
* [PyQt5](https://pypi.org/project/PyQt5/)
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

All dependencies can be downloaded with pip:
```
pip install [name]
```

## Pyqt5 Designer
The gui is written in pyqt5 designer. This is a tool that can be downloaded via [pip](https://pypi.org/project/pyqt5-tools/) or directly for [windows and mac](https://build-system.fman.io/qt-designer-download) or [linux](https://pythonbasics.org/qt-designer-python/)

### Lines that need to be copied from earlier versions 
* All button connection stuff
* Autocompleters start with the init, ish line 89
* setCompleter -> add for all lineEdit that should have it
* addItems -> add for all comboBox that should have it
* Change "setHtml" to "updateStatus"
* init

### Other stuff 
* set "resize" to "setFixedSize"
* Set right tab size on everything
* Point size stuff => comment out all "font.setPointSize(-1)"
* Fix imagepath

To make ui file to py file: (seems to not work?)
```
start python -m PyQt5.uic.pyuic furniture-counter.ui -o main.py -x
```
or 
```
pyuic5 furniture-counter.ui -o main.py -x
```
This will need pyqt5-tools

## Compiling
To recompile use
```
python -m PyInstaller -F main.pyw
```
### To think about when compiling
It is a good idea to remove the src map, and putting everything on the same level. This will take away the need for a folder when using main. When doing this remember to rewrite the path to find the images. This is to be able to have the images in a folder instread for on the same level as main program.

To remove the dotenv. With this it is meant to copy the .env directly in the database file. This will hide the password a little more. This is not very secure but better than having passwords directly in a file to see for everyone.


Note that [pyinstaller](https://pypi.org/project/pyinstaller/) need to be downloaded from pip to comppile:
```
pip install pyinstaller
```
