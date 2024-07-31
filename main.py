from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/convert', methods=['POST'])
def convert_html_to_text():
    try:
        # Get the HTML-encoded text from the request
        data = request.json
        html_encoded_text = data.get('text', '')

        # Create a prompt for the OpenAI API to convert HTML to plain text
        prompt = f"Convert the following HTML-encoded text to plain text:\n\n{html_encoded_text}"

        # Call the OpenAI API to get the conversion result
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Replace with the appropriate model if needed
            prompt=prompt,
            max_tokens=500,  # Adjust the number of tokens as needed
            temperature=0.2  # Set temperature for less randomness
        )

        # Extract the plain text from the response
        plain_text = response.choices[0].text.strip()

        # Return the plain text in JSON format
        return jsonify({'plain_text': plain_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
