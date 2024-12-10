from flask import Flask, request, jsonify, redirect, session, url_for
from flask_cors import CORS
from openai_service import generate_exam_questions
from canvas_service import create_canvas_quiz, get_courses_info
from config import Config
from dotenv import load_dotenv
import os
import requests

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def login():
#     auth_url = f"{Config.CANVAS_API_URL}/login/oauth2/auth"
#     params = {
#         "client_id": Config.CANVAS_CLIENT_ID,
#         "response_type": "code",
#         "redirect_uri": Config.REDIRECT_URI,
#     }
#     request_url = requests.Request('GET', auth_url, params=params).prepare().url
#     return redirect(request_url)

# @app.route('/callback')
# def callback():
#     code = request.args.get('code')
#     token_url = f"{Config.CANVAS_API_URL}/login/oauth2/token"
#     data = {
#         "grant_type": "authorization_code",
#         "client_id": Config.CANVAS_CLIENT_ID,
#         "client_secret": Config.CANVAS_CLIENT_SECRET,
#         "redirect_uri": Config.REDIRECT_URI,
#         "code": code,
#     }
    
#     # Intercambio de código por token
#     response = requests.post(token_url, data=data)
#     token_response = response.json()
#     access_token = token_response.get('access_token')
    
#     # Guardar el token en la sesión
#     session['access_token'] = access_token
    
#     return "Login exitoso! Puedes usar este token para llamar a la API de Canvas."

@app.route('/api/generate_exam', methods=['POST'])
def generate_exam():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    questions = generate_exam_questions(prompt)
    return questions

@app.route('/api/create_quiz', methods=['POST'])
def create_quiz():
    data = request.json
    course_id = data.get('course_id')
    questions = data.get('questions')
    title = data.get('title') # cambio 101224
    description = data.get('description') # cambio 101224
    
    if not course_id or not questions:
        return jsonify({"error": "Ingresar ID del curso y preguntas"}), 400

    quiz_id = create_canvas_quiz(
        course_id, 
        questions,
        title, # cambio 101224
        description #cambio 101224
        )
    return jsonify({"message": "Quizz creado exitosamente", "quiz_id": quiz_id})

# @app.route('/api/courses', methods=['GET'])
# def courses():
#     courses_info = get_courses_info()
#     return jsonify(courses_info)


# Método POST requiere que se ejecute cuando se ingrese como input 
# el api_key en front
@app.route('/api/courses', methods=['POST'])
def courses():
    data = request.json
    api_key = data.get('api_key')  # { "api_key": "your_canvas_api_key" }

    if not api_key:
        return jsonify({"error": "API key is required"}), 400

    courses_info = get_courses_info(api_key)
    return jsonify(courses_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)

## se envia el string con la llave de canvas
@app.route('/api/keys', methods=['POST'])
def api_key():
    data=request.json
    apikey=data.get('apikey')
    return jsonify({"api_key":apikey})