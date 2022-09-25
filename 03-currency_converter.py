import requests
from bs4 import BeautifulSoup
from PyQt6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget)

CURRENCIES = ["USD", "MXN", "EUR"]


def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", {"class": "ccOutputRslt"}).get_text()
    rate = float(rate[:-4])

    return rate


def show_currency():
    input_text = float(text.text())
    in_currency = in_combo.currentText()
    target_currency = target_combo.currentText()
    rate = get_currency(in_currency, target_currency)
    output = round(input_text * rate, 2)
    message = f"{input_text} {in_currency} = {output} {target_currency}"
    output_label.setText(message)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()

in_combo = QComboBox()
in_combo.addItems(CURRENCIES)
layout.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(CURRENCIES)
layout.addWidget(target_combo)

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
