import random
from words import list1

width='*'*40
print(f"{width}Guess The Word{width}")
name=input('Pls enter your name:')
def working(turn,guess_start,word):
	while turn>0:
		failed=0
		for char in word:
			if char==guess_start:
				print(char)
			else:
				print('_')
				failed +=1
			
		if failed==0:
			print(f'Congrats {name} u won the game')
			print(f"{width}The word was {word}{width}")
		uguess=input('enter yr guess::')
		guess_start +=uguess
		if uguess not in word:
			turn -=1
			print(f"it's wrong u have {turn} turns left ")
		if turn==0:
			print(f'Oops! {name} u lose,well u can try again')
			print(f"{width}The word was {word}{width}")
	return main()

def main():
	print(f"{width}Guess The Word{width}")
	print('1.Press 1 to play the game')
	print('2.Press 2 to exit')
	ask=int(input('Pls Enter Yr choice::'))
	if ask==1:
		print(f'Ok {name},let us start the game')
		return working(8,'',random.choice(list1))
	if ask==2:
		print(f'Bye {name},see ya!!')
main()