from flask import Blueprint, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()

chatgpt_bp = Blueprint('chatgpt_bp', __name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@chatgpt_bp.route('/generate-flowchart', methods=['POST'])
def generate_flowchart():
    """
    Envia um prompt para gerar dados de fluxograma.
    ---
    tags:
      - AI 
    parameters:
      - in: body
        name: body
        description: O prompt que o usuário deseja enviar a nossa IA
        schema:
          type: object
          required:
            - prompt
          properties:
            prompt:
              type: string
              example: "Gostaria de criar um fluxograma de pagamento..."
    responses:
      200:
        description: Resposta gerada pelo ChatGPT
        schema:
          type: object
          properties:
            response:
              type: string
              example: "Gerando fluxograma..."
    """
    data = request.json
    user_prompt = data.get('prompt', '')

    full_prompt = (f"Você precisa devolver dados importantes para montar o fluxograma.\n"
                   f"Prompt que o usuário vai mandar: {user_prompt}")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_prompt,
        max_tokens=300,
        temperature=0.7
    )

    generated_text = response.choices[0].text.strip()

    return jsonify({"response": generated_text})
