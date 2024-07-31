from html import unescape
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_html_to_text():
    try:
        data = request.json
        html_encoded_text = data.get('text', '')
        # Decode HTML entities
        decoded_text = unescape(html_encoded_text)
        # Replace <br /> tags with newline characters
        text_with_newlines = re.sub(r'<br\s*/?>', '\n', decoded_text)
        # Remove any remaining HTML tags
        plain_text = re.sub(r'<[^>]+>', '', text_with_newlines)
        return jsonify({'plain_text': plain_text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
