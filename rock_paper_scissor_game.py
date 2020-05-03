import random
rk="rock"
pa="paper"
sc="scissor"
width=('*'*20)
header=f'{width}welcome to game of rock paper and scissorsss uhooooooooooooooooooooooooo{width}'
hashtag=f'{width}work by flashh{width}'
def repeat():
	a=input("what is yr move,rock or paper or scissorsss::")
	b=['rock','paper','scissor']
	comp=(random.choice(b))
	print(f"my choice::{comp}")
	get=comp
	if a==rk and get==sc:
		print('u won')
	elif a==sc and get==pa:
		print('u won')
		
	elif a==pa and get==rk:
		print('u won')
	elif a==pa and get==pa:
		print("it is a tie")
	elif a==sc and get==sc:
		print('it is a tie')
	elif a==rk and get==rk:
		print('it is a tie')
	else:
		print('ko i won asshlol')
	return main()

def main():
	print(header)
	print(hashtag)
	print('1.press 1 to play game')
	print('2.press 2 to exit')
	take=int(input('enter choice::'))
	if take==1:
		return repeat()
	elif take==2:
		print(':) Bye Byeeeee,Come back soon :)')
	else:
		print('wrong choice fkr')
main()
