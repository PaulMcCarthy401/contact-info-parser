import os
import spacy


nlp = spacy.load('en_core_web_sm')

class ContactInfo:
	def __init__(self, name, phoneNumber, emailAddress):
		self.name = name
		self.phoneNumber = phoneNumber
		self.emailAddress = emailAddress

def getContactInfo(document):
	"""Parse a document and return a ContactInfo object containing parsed values
	
	Args:
		document (str): The raw contact info string
	
	Returns:
		ContactInfo
	"""
	name = ''
	phoneNumber = ''
	emailAddress = ''

	for line in document.split('\n'):
		doc = nlp(line)
		
		for ent in doc.ents:
			if ent.label_ == 'PERSON':
				return ent.text