import requests
from bs4 import BeautifulSoup
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)


def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", {"class": "ccOutputRslt"}).get_text()
    rate = float(rate[:-4])

    return rate


def show_currency():
    input_text = float(text.text())
    rate = get_currency("USD", "MXN")
    output = round(input_text * rate, 2)
    output_label.setText(str(output))


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Convert')
btn.clicked.connect(show_currency)
layout.addWidget(btn)

output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
