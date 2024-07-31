from html import unescape
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_html_to_text():
    data = request.json
    html_encoded_text = data.get('text', '')
    plain_text = unescape(html_encoded_text)
    return jsonify({'plain_text': plain_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
