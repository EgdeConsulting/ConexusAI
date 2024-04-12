from flask import Blueprint, request, jsonify
import openai
import os
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
main = Blueprint('main', __name__)

@main.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    user_message = data.get('prompt')

    # Sjekk om brukermeldingen faktisk ble mottatt
    if not user_message:
        return jsonify({"error": "Ingen melding mottatt"}), 400

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_message},
            ],
            model="gpt-3.5-turbo",
        )
        answer = chat_completion.choices[0].message.content
        return jsonify({"answer": answer}), 200
    except Exception as e:
        # Returnerer en feilmelding og en 500 Internal Server Error statuskode hvis noe går galt.
        return jsonify({"error": f"En feil oppstod: {str(e)}"}), 500
        
        
        
@main.route('/queryss', methods=['POST'])
def handle_queryss():
    data = request.json
    user_message = data.get('prompt')

    # Sjekk om brukermeldingen faktisk ble mottatt
    if not user_message:
        return jsonify({"error": "Ingen melding mottatt"}), 400

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_message},
            ],
            model="gpt-3.5-turbo",
        )
        answer = chat_completion.choices[0].message.content
        return jsonify({"answer": answer}), 200
    except Exception as e:
        # Returnerer en feilmelding og en 500 Internal Server Error statuskode hvis noe går galt.
        return jsonify({"error": f"En feil oppstod: {str(e)}"}), 500