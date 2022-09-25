from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)


def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize() + '.')


app = QApplication([])
window = QWidget()
window.setWindowTitle('Sentence Maker')

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Make Sentence')
btn.clicked.connect(make_sentence)
layout.addWidget(btn)

output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
