from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QFileDialog, QLabel, QPushButton,
                             QVBoxLayout, QWidget)


def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select files")
    message.setText('\n'.join(filenames))


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, "wb") as f:
            f.write(b"")
        path.unlink()
    message.setText("Files destroyed successfully!")


app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')
layout = QVBoxLayout()

description = QLabel(
    'Select the files you want to destroy. The files will be <font color="red">permanently</font> deleted.')
layout.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip('Open File')
open_btn.setFixedWidth(100)
open_btn.clicked.connect(open_files)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)

destroy_btn = QPushButton('Destroy Files')
destroy_btn.setFixedWidth(100)
destroy_btn.clicked.connect(destroy_files)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()
