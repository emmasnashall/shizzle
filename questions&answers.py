question='What is your name?'
print(question)
answer= raw_input()
print('Hello ' + answer + ', my name is Jubjub')
question_2="I can guess the length of any word. Try me!"
print(question_2)
answer_2 = raw_input()
print('that was ' + str(len(answer_2)) + ' characters long')
question_3='What is your favourite animal sound?'
print(question_3)
answer_3=raw_input() + " "
question_4= 'Great! What is your favourite number?'
print(question_4)
answer_4=raw_input()
print(answer_3 * int(answer_4))