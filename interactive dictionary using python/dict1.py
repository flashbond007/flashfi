import json
from difflib import get_close_matches
data=json.load(open('data.json'))

def value():
	word=input('Enter a word : ')
	word=word.lower()
	if word in data:
		print(data[word])
		main()
	elif word not in data:
		new_data=get_close_matches(word,data,1,0.6)
		take=input((f'do u wanna search for {new_data}, y for Yes and n for NO::'))
		if take=='y':
			new_data=' '.join(map(str, new_data))  
			print(data[new_data])
			main()
		else:
			print('Fine then cut loo')

	else:
		print('Pls chk the word')
		return main()

def main():
	print('1.Enter to search for a word')
	print('2.Enter to exit')
	choice=int(input('Enter your choice from above menu:: '))
	if choice==1:
		return value()
	elif choice==2:
		print('Cut lo furtiii mein!!!!!')
	else:
		print('Andheee!!!!')
main()