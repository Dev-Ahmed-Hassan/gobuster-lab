from flask import Flask, abort, send_from_directory
app = Flask(__name__, static_folder='.')

@app.route('/')
def home():
    return open('index.html', 'r', encoding='utf-8').read()

@app.route('/forbidden')
def forbidden():
    abort(403)

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
