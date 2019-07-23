from flask import Flask, url_for, render_template, request, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template("add.html", **context)
