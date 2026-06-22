from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    html_output = ""

    if request.method == 'POST':
        text = request.form['text']
        tag = request.form['tag']
        html_output = f"<{tag}>{text}</{tag}>"

    return render_template('index.html', html_output=html_output)

if __name__ == '__main__':
    app.run(debug=True)