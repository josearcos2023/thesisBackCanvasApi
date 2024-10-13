from canvasapi import Canvas
from config import Config

canvas = Canvas(Config.CANVAS_API_URL, Config.CANVAS_API_KEY)

def create_canvas_quiz(course_id, questions):
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    # Crear el quiz en Canvas
    quiz = course.create_quiz({
        'title': 'Generated Quiz',
        'description': 'Quiz generated from AI questions',
        'quiz_type': 'assignment',
        'time_limit': 30,
        'published': True
    })

    # Añadir las preguntas al quiz
    for question in questions:
        quiz.create_question({
            'question_name': question['question_name'],
            'question_text': question['question_text'],
            'question_type': 'multiple_choice_question',
            'points_possible': 10,
            'answers': question['answers']
        })

    return quiz.id
