print('\nQuiz')

take_quiz = 'y'
question = 1
correct = 0
incorrect = 0
answer = ''

quiz = {'2 + 2':4, '1 + 4':5, '5 * 5':25, '9 - 6':3, '11 - 3':8, 
'24 / 8':3, '10 + 5':15, '7 * 7':49, '8 / 4':2, '25 * 4':100, '12 * 12':144, '24 - 10':14}


while question <= 10:
    key, value = quiz.popitem()
    print(key)
    answer = int(input('enter answer: '))
    if answer == value:
        correct += 1
    else:
        incorrect += 1
    question += 1
print()
print('Total correct: ', correct)
print('Total incorrect: ', incorrect)

