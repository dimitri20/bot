from flask import Flask, render_template, request
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/', methods=['POST', 'GET'])
def index():
    tasks = ''
    form = CommandForm()
    return render_template('index.html', form=form, results=results)


if __name__ == "__main__":
    app.run(debug=True)
