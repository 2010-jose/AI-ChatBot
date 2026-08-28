from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

# Configure sua permissão
client = genai.Client(api_key='API_KEY')

# Lista para guardar o histórico (zera se reiniciar o servidor)
historico_chat = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        
        # Adiciona sua pergunta ao histórico
        historico_chat.append({"role": "user", "text": pergunta})

        # Chama a API do Gemini
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=(pergunta)
        )
        
        # Adiciona a resposta da IA ao histórico
        historico_chat.append({"role": "bot", "text": response.text})

    return render_template('index.html', chat=historico_chat)

if __name__ == '__main__':
    app.run(debug=True)
