from flask import Flask, request, jsonify
from openai_service import generate_exam_questions
from canvas_service import create_canvas_quiz
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Ruta para generar preguntas del examen usando OpenAI
@app.route('/generate_exam', methods=['POST'])
def generate_exam():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    questions = generate_exam_questions(prompt)
    return questions

# Ruta para crear un quiz en Canvas con las preguntas generadas
@app.route('/create_quiz', methods=['POST'])
def create_quiz():
    data = request.json
    # course_id = data.get('course_id')
    course_id = data.get('course_id')
    questions = data.get('questions')

    if not course_id or not questions:
        return jsonify({"error": "Course ID and questions are required"}), 400

    quiz_id = create_canvas_quiz(course_id, questions)
    return jsonify({"message": "Quiz created successfully", "quiz_id": quiz_id})

if __name__ == "__main__":
    app.run(debug=True)
