import ocrparser


def promptModel(choices):
	"""Prompt the user with a list of numbered choices and return the choice.
	
	Args:
		choices (dict): A dictionary of key-value choices
	
	Returns:
		String: the selected choice
	"""
	while True:
		print("Select a spacy model:")
		for key, choice in choices.items():
			print("\t{}. {}".format(key, choice))

		selectedKey = input()
		if selectedKey in choices.keys():
			return choices[selectedKey]
		else:
			print("Invalid choice.\n")

choices = {
	'1': 'en_core_web_sm',
	'2': 'en_core_web_md',
	'3': 'en_core_web_lg',
}

model = promptModel(choices)

with open('example.txt') as file:
	data = file.read()

	# split each card by double newlines
	cards = data.split('\n\n')
	
	# set up the card parser with a chosen model
	cardParser = ocrparser.BusinessCardParser(model)

	for card in cards:
		contactInfo = cardParser.getContactInfo(card)
		print(contactInfo, '\n')