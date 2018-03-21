import spacy


class ContactInfo:
	def __init__(self, name, phoneNumber, emailAddress):
		self.name = name
		self.phoneNumber = phoneNumber
		self.emailAddress = emailAddress

class BusinessCardParser:
	def __init__(self, model='en_core_web_sm'):
		self.nlp = spacy.load(model)

	def getContactInfo(self, document):
		"""Parse a document and return a ContactInfo object containing parsed values
		
		Args:
			document (str): The raw contact info string
		
		Returns:
			ContactInfo
		"""
		for line in document.split('\n'):
			doc = self.nlp(line)
			
			for ent in doc.ents:
				if ent.label_ == 'PERSON':
					return ent.text