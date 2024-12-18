from canvasapi import Canvas
from config import Config
# import json

canvas = Canvas(Config.CANVAS_API_URL, Config.CANVAS_API_KEY)

## cursos disponibles
# courses = canvas.get_courses()

def create_canvas_quiz(
    course_id, 
    questions, 
    title,
    description
    ):
    
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    # quiz_params = {
    #     'title': 'Generated Quiz 1',
    #     'description': 'A quiz generated by AI.', 
    #     'quiz_type': 'assignment',
    #     'published': True,
    #     'question_types':['multiple_choice']
    # }
    
    # parametros con titulo y descripcion
    quiz_params = {
        'title': title,
        'description': description,
        'quiz_type': 'assignment',
        'published': True,
        'question_types':['multiple_choice']
    }
    
    # Crea el quiz en el curso
    quiz = course.create_quiz(quiz_params)

    # print(questions)

    # Añadir las preguntas al quiz
    for question in questions:
        question_params = {
            'question_text': question['question_text'],
            'question_type': 'multiple_choice_question',
            'points_possible': 2,
            'answers': []
        }
        
        # print(question['question_text'])
        # Crea la lista de respuestas
        for answer in question['answers']:
            answer_data = {
                'text': answer['answer_text'],
                'weight': 100 if answer['correct'] else 0
            }
            
            # print(answer['answer_text'])
            
            question_params['answers'].append(answer_data)
            # question_params['question']['answers'].append(answer_data)

        # print(f"Question Params: {question_params}")
        
        # print(question_params)
        # print("----------------")
        # Agrega la pregunta al quiz
        # quiz.create_question(**question_params)
        quiz.create_question(question=question_params)
        # quiz.create_question(question_params)
    
    ## listado de cursos disponibles
    # for course in courses:
    #     print(f"ID: {course.id}, Nombre: {course.name}")
    
    return quiz.id
    # return question_params

# #Obtener los cursos e ID de cursos
# def get_courses_info():
#     courses = canvas.get_courses()
#     courses_info = []
    
#     for course in courses:
#         courses_info.append({
#             'id': course.id,
#             'name': course.name
#         })
    
#     return courses_info

#  Cuando se envie la apikey mediante el metodo POST courses()
def get_courses_info(api_key):
    
    canvas = Canvas(Config.CANVAS_API_URL, api_key)
    courses = canvas.get_courses()
    courses_info = []
    
    for course in courses:
        courses_info.append({
            'id': course.id,
            'name': course.name
        })
    
    return courses_info