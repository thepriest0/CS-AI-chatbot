from flask import Flask, request, jsonify, render_template_string
import openai
import os

app = Flask(__name__)

# Get the OpenAI API key from environment variables
openai.api_key = os.getenv('sk-proj-RfcgbsHDIDPjeKTRtoWWT3BlbkFJEBIgCXao6n0dV2CQHUyg')

# Read the HTML file and store its content in a variable
with open('index.html', 'r') as file:
    html_content = file.read()

@app.route('/')
def index():
    return render_template_string(html_content)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data['question']
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    answer = response.choices[0].text.strip()
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
