import ocrparser
import timeit
from utils.prompt import promptQuestion, promptBoolean


modelChoices = {
	'1': 'en_core_web_sm',
	'2': 'en_core_web_md',
	'3': 'en_core_web_lg',
}

yesOrNoChoices = {'1': 'Yes', '2': 'No'}

model = promptQuestion('\nSelect a spacy model:', modelChoices)
isTimed = promptBoolean('Would you like to time the parsing?')

if isTimed:
	iterations = promptQuestion('How many iterations (higher => more accurate, but slower)',
		{'1': 10, '2': 100, '3': 250})

isPrintAll = promptBoolean('Show all matches? (i.e., not just first found)')


with open('example.txt') as file:
	data = file.read()

	# split each card by double newlines
	cards = data.split('\n\n')
	
	# set up the card parser with a chosen model
	print("\nLoading model...")
	cardParser = ocrparser.BusinessCardParser(model)

	print("\n=>\n")

	for index, card in enumerate(cards):
		# Time the parser for each document
		if isTimed:
			print("Timing, please wait...")
			total_time = timeit.timeit(
				'cardParser.getContactInfo(card)', number=iterations, globals=globals())

			print("\tCard parsing took ", total_time / iterations,
				"seconds on average over", iterations, "iterations")

		# attempt to parse the contact info and display
		contactInfo = cardParser.getContactInfo(card, isPrintAll)
		print(contactInfo, '\n')