from flask import Flask, request, jsonify
from flask_cors import CORS
from openai_service import generate_exam_questions
from canvas_service import create_canvas_quiz, get_courses_info
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app)

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
    # print(questions)
    if not course_id or not questions:
        return jsonify({"error": "Ingresar ID del curso y preguntas"}), 400

    quiz_id = create_canvas_quiz(course_id, questions)
    return jsonify({"message": "Quizz creado exitosamente", "quiz_id": quiz_id})

@app.route('/api/courses', methods=['GET'])
def courses():
    courses_info = get_courses_info()
    return jsonify(courses_info)

if __name__ == "__main__":
    app.run(debug=True)
