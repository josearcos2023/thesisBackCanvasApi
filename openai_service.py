from textwrap import dedent
import openai
import json
from pydantic import BaseModel
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def generate_exam_questions(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=
            [
				{ "role": 'system', "content": 'You are a helpful assistant.' },
				{ "role": 'user', "content": prompt },
			],
        temperature= 0,
        max_tokens= 800,
        top_p= 1,
        frequency_penalty= 0.0,
        presence_penalty= 0.0,
        # stop= ['/'],

        response_format={
            "type":"json_schema",
            "json_schema":{
                "name":"description",
                "schema":{
                    "type":"object",
                    "properties": {
                        "questions":{
                            "type":"array",
                            "items":{
                                "type":"object",
                                "properties":{
                                    "question": {"type": "string"},
                                    "answer": {"type": "string"},
                                    "output": {"type": "string"}
                                },
                                "required":["question","answer","output"],
                                "additionalProperties":False
                            }
                        },
                    },
                    "required":["questions"],
                    "additionalProperties": False
                },
                "strict":True
            }
        }
    )


    questions_text = response.choices[0].message.content

    questions = parse_questions(questions_text)
    # print(questions)
    return questions
    # return questions_text

def parse_questions(questions_text):
    questions_data = json.loads(questions_text)

    questions = []

    for item in questions_data['questions']:
        question_text = item['question']
        correct_answer = item['answer']
        output = item['output'].split('\n')

        answers = []
        for option in output:
            answer_text = option.strip()
            is_correct = correct_answer in answer_text
            answers.append({
                "answer_text": answer_text,
                "correct": is_correct
            })

        question = {
            "question_text": question_text,
            "answers": answers
        }

        questions.append(question)

    return questions
