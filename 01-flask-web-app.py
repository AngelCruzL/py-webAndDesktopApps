from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def home_post():
    dim1 = request.form['first_dim']
    dim2 = request.form['second_dim']
    dim3 = request.form['third_dim']
    volume = float(dim1)*float(dim2)*float(dim3)
    return render_template('index.html', output=volume, dim_1=dim1, dim_2=dim2, dim_3=dim3)


app.run(host='localhost', port=5000, debug=True)
