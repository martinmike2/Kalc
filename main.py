import sys

import krpc
from PyQt5 import QtWidgets

from Forms.Ui import Ui

# connection = krpc.connect("Test", "127.0.0.1", 50000, 50001)

app = QtWidgets.QApplication(sys.argv)
window = Ui(krpc)
app.exec_()
