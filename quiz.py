import time

print('Would you take the quiz')
print('print yes if take the quiz')
yes = input()

if yes == 'yes':
	print('Ok lets Start!')
	time.sleep(2)
	print('Ok,first question What is the formula of glucose')
	first = input()
else:
	print("exiting!")
	exit()
if first == 'C6,H12,O22' or 'C6H12O22':
	print('Correct!,next question')
	time.sleep(2)
	print('Second question,What is the percentage of water in southern hemisphere?')
	second = input()
else:
	print('Wrong')
	exit()
if second == '56 percent' or '56 %':
	print('Correct!')
	print('Last question!')
	time.sleep(2)
	print('What is sial?')
	third = input()
else:
	print('Wrong')
if third == 'aluminium' or 'aluminum':
	print('Correct!')
	print('you answered all the question right keep it up.')
	exit()