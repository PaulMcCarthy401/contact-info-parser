import spacy
import re


class ContactInfo:
	def __init__(self, name, phoneNumber, emailAddress):
		self.name = name
		self.phoneNumber = phoneNumber
		self.emailAddress = emailAddress
	
	def __str__(self):
		"""
		Format:
		
		Name: <name>
		Phone: <phoneNumber>
		Email: <emailAddress>
		"""
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

	def getPhoneNumber(self, text, excludeFax=True):
		"""Parse a single card and return a string containing the phone number,
			or None, if no phone number was found. The phone number will be
			returned without formatting."""

		"""Regex: (where brackets indicated matches)

		^(?!Fax).*(?:\d{1,3}.*)?\d{3}.*\d{3}.*\d{4}


		^(?!Fax).* - OPTIONAL - Exclude strings which start with "Fax"

		(?:\d{1,3}.*)? - Include area code in match, if it exists
			Ex. [1]-123-456-7890

		\d{3}.* - Match block of 3 numbers:
			Ex. [123]-[456]-7890

		\d{3}.* - Match block of 3 numbers:
			Ex. 123-456-[7890]
		"""
		if excludeFax:
			match = re.search(r'^(?!Fax).*(?:\d{1,3}.*)?\d{3}.*\d{3}.*\d{4}', text)
		else:
			match = re.search(r'(?:\d{1,3}.*)?\d{3}.*\d{3}.*\d{4}', text)
		
		if match:
			# return the phone number without formatting (only numeric values)
			return re.sub('[^0-9]', '', match.group())
		return None


	def getEmailAddress(self, text):
		"""Parse a string and return a string containing the email address,
			or None, if no email address was found."""

		"""Regex: (where brackets indicated matches)

		Description: Match strings where non-whitespace characters
		surround an @ symbol.
		Ex: "Email: [john.doe@example.com] test"

		[^\s]*@[^\s]*

		[^\s]* - Match any characters which are not whitespace
		"""
		match = re.search(r'[^\s]*@[^\s]*', text)

		if match:
			# return the matched email address
			return match.group()
		return None

	def getContactInfo(self, document, showMatches=False):
		"""Parse a document and return a ContactInfo object.
			Object values will contain either the respective
			info or None if no info could be found.
		
		Args:
			document (str): The raw contact info string
			showMatches (bool): If true, prints all contact info detected
		
		Returns:
			ContactInfo
		"""
		names = []
		phoneNumbers = []
		emailAddresses = []

		# parse through document line by line
		# and gather possible contact info fragments
		for line in document.split('\n'):
			matchedName = self.getName(line)
			if matchedName:
				names.append(matchedName)

			matchedPhoneNumber = self.getPhoneNumber(line)
			if matchedPhoneNumber:
				phoneNumbers.append(matchedPhoneNumber)

			matchedEmailAddress = self.getEmailAddress(line)
			if matchedEmailAddress:
				emailAddresses.append(matchedEmailAddress)
		
		# For purposes of the challenge, the showMatches parameter
		# allows the tester to display all info captured by this parser.
		#
		# In production code, this functionality should be
		# seperated from this method.
		#
		if showMatches:
			print("- Matched names: ", names)
			print("- Matched phone numbers: ", phoneNumbers)
			print("- Matched email addresses", emailAddresses)
		
		return ContactInfo(names[0], phoneNumbers[0], emailAddresses[0])
		