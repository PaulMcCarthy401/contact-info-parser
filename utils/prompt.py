def promptQuestion(prompt, choices, boolean=False):
	"""Prompt the user with a list of numbered choices and return the choice.
	
	Args:
		choices (dict): A dictionary of key-value choices
	
	Returns:
		String: the selected choice
	"""
	while True:
		print(prompt)
		for key, choice in choices.items():
			print("\t{}. {}".format(key, choice))

		selectedKey = input()
		if selectedKey in choices.keys():
			return choices[selectedKey]
		else:
			print("Invalid choice.\n")


def promptBoolean(prompt):
	yesChoices = ['yes', 'y', '1']
	noChoices = ['no', 'n', '2', '']
	
	while True:
		print(prompt, '(y/n)')

		selectedKey = input()
		if selectedKey in yesChoices:
			return True
		elif selectedKey in noChoices:
			return False
		else:
			print("Invalid choice.\n")