#!/usr/bin/env python3

class Quiz(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

        with open(name) as file:
            for line in file:
                if len(line.strip()) == 0:
                    continue

                question = tuple(string.strip() for string in tuple(line.split("    ")))
                if question[1].startswith("{"):  # handle multiple choice
                    question = (question[0], tuple(((question[1])[1:-1]).split(", ")), question[2])
                question = (question[0], question[1], tuple(((question[2])[1:-1]).split(": ")))  # unpack embed
                self.questions.append(question)

    def __iter__(self):
        def questions_gen(questions):
            current = 0

            while current < len(questions):
                yield questions[current]
                current += 1

        return questions_gen(self.questions)
