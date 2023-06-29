from flask import Flask, render_template, request
import mistune
from flask import redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        content = request.form.get('content')
        html_content = mistune.markdown(content)
        return render_template('gist.html', content=html_content)
    return render_template('create.html')

if __name__ == '__main__':
    app.run()
