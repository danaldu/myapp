from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    text = request.json['text']
    return jsonify({'result': text})

if __name__ == '__main__':
    app.run(debug=True)