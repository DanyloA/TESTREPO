def what_integer_bigger(first_integer,second_integer):
	if first_integer > second_integer:
		return first_integer
	else:
		return second_integer
print(what_integer_bigger(1123,1232))

def integers(string):
	answer=0
	for i in string:
		if i.isdigit():
			answer+=1
	return answer
print(integers('dkwfwefwehfwgehgwefvgwevgfwefwef76we75fw7e5f5wef57we5fwe57f5wef5w7ef5we65fw5ef57ewf5wef57wefw7ef5wef6we6fwe5f5wef756wef7'))
