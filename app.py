from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'main_page.html')

@app.route('/chinese')
def chinese():
    return send_from_directory('.', 'cute_chinese.html')

@app.route('/math')
def math():
    return send_from_directory('.', 'math_game.html')

if __name__ == '__main__':
    app.run(debug=True) 