import json

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout, QWidget)

data = json.load(open("data/dictionary.json"))


def translate():
    w = text.text()
    w = w.lower()
    if w in data:
        results = data[w]
        output_label.setText("\n".join(results))
    else:
        output_label.setText("The word doesn't exist. Please double check it.")


app = QApplication([])
window = QWidget()
window.setWindowTitle('Word Definition')

layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

layout2 = QVBoxLayout()
layout.addLayout(layout2)

text = QLineEdit()
layout1.addWidget(text)

btn = QPushButton('Convert')
layout1.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(translate)

output = QWidget()

output_label = QLabel('')
output_label.setFixedSize(600, 50)
layout2.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
