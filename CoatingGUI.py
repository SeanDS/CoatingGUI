#!/usr/bin/env python
# This work is licensed under the Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative
# Commons, PO Box 1866, Mountain View, CA 94042, USA.

import sys
import argparse
from gui.mainWindow import MainWindow
from qtpy import QtWidgets

qApp = QtWidgets.QApplication(sys.argv)

parser = argparse.ArgumentParser(prog='CoatingGUI.py')
parser.add_argument('-p', '--project', help='open CoatingGUI project file PROJECT')
args = parser.parse_args()
Window = MainWindow(vars(args))
Window.show()
qApp.exec_()