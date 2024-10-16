from canvasapi import Canvas
from config import Config

canvas = Canvas(Config.CANVAS_API_URL, Config.CANVAS_API_KEY)

def create_canvas_quiz(course_id, questions):
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    quiz_params = {
        'title': 'Generated Quiz',
        'description': 'A quiz generated by AI.',
        'quiz_type': 'assignment',
        'published': True
    }
    
    # Crea el quiz en el curso
    quiz = course.create_quiz(quiz_params)

    # Añadir las preguntas al quiz
    for question in questions:
        question_params = {
            'question_name': question['question_text'],
            'question_type': 'multiple_choice_question',
            'points_possible': 1,
            'answers': []
        }

        # Crea la lista de respuestas
        for answer in question['answers']:
            answer_data = {
                'text': answer['answer_text'],
                'weight': 100 if answer['correct'] else 0
            }
            question_params['answers'].append(answer_data)

        # Agrega la pregunta al quiz
        quiz.create_question(**question_params)

    return quiz.id
    # return question_params