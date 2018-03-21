import spacy
import re


class ContactInfo:
	def __init__(self, name, phoneNumber, emailAddress):
		self.name = name
		self.phoneNumber = phoneNumber
		self.emailAddress = emailAddress
	
	def __str__(self):
		return "Name: {}\nPhone: {}\nEmail: {}".format(
			self.name, self.phoneNumber, self.emailAddress
		)

class BusinessCardParser:
	def __init__(self, model='en_core_web_sm'):
		try:
			self.nlp = spacy.load(model)
		except:
			raise ImportError("Spacy model could not be loaded.")
	
	def getName(self, text):
		"""Parse a string and return a NER identified name,
			or None, if no name was found."""

		# parse text into spacy nlp document
		doc = self.nlp(text)
		
		# check through detected entities for those labeled "PERSON",
		# return the first correctly labeled token found
		for ent in doc.ents:
			if ent.label_ == 'PERSON':
				return ent.text

		return None

	def getPhoneNumber(self, text):
		"""Parse a single card and return a string containing the phone number,
			or None, if no phone number was found. The phone number will be
			returned without formatting."""
		match = re.search(r'(?:\d{1,3}.*)?\d{3}.*\d{3}.*\d{4}', text)
		
		if match:
			return re.sub('[^0-9]', '', match.group())
		return None


	def getEmailAddress(self, text):
		"""Parse a string and return a string containing the email address,
			or None, if no email address was found."""
		match = re.search(r'[^\s]*@[^\s]*', text)

		if match:
			return match.group()
		return None

	def getContactInfo(self, document):
		"""Parse a document and return a ContactInfo object.
			Object values will contain either the respective
			info or None if no info could be found.
		
		Args:
			document (str): The raw contact info string
		
		Returns:
			ContactInfo
		"""
		name = None
		phoneNumber = None
		emailAddress = None

		# parse each line for contact info, saving the first
		# match if one is found.
		for line in document.split('\n'):
			matchedName = self.getName(line)
			if matchedName:
				name = matchedName

			matchedPhoneNumber = self.getPhoneNumber(line)
			if matchedPhoneNumber:
				phoneNumber = matchedPhoneNumber

			matchedEmailAddress = self.getEmailAddress(line)
			if matchedEmailAddress:
				emailAddress = matchedEmailAddress
		
		return ContactInfo(name, phoneNumber, emailAddress)
		