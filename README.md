# contact-info-parser
A business card info parser for arbitrary contact info, built with Python 3 and spaCy.

# Requirements
 - Python 3.4+
 - cython build environment

     Because spaCy requires certain components be built with cython (for speed),
     some tools must be available before installation. Steps are linked in the
     following section.

## Installation
The following steps are done via a terminal/command prompt.

1. Install build dependencies
   - [Ubuntu](https://spacy.io/usage/#source-ubuntu)
   - [macOS/OS X](https://spacy.io/usage/#source-osx)
   - [Windows](https://spacy.io/usage/#source-windows)
   - Fedora `sudo dnf install python-devel git`

2. Pull down the Github repo
   ```
   git clone https://github.com/PaulMcCarthy401/contact-info-parser.git
   ```

3. Set up a python virtual environment
   ```
   python3 -m venv env
   ```

4. Switch into the python environment
   - Windows `env\Scripts\activate`
   - Linux/Mac `source env/bin/activate`

5. Install dependencies
   ```
   pip install -r requirements.txt
   ```
   **Important**: Ensure that before installing dependencies (step 5) that you
   have completed step 1 (installing build dependencies). This step
   will fail if that step was not completed.

   *Generic installation instructions can be found [here](https://spacy.io/usage/#pip)*
   *since spaCy is the only dependency.*

6. Choose a model
   - Small:  `python3 -m spacy download en_core_web_sm`
   - Medium: `python3 -m spacy download en_core_web_md`
   - Large:  `python3 -m spacy download en_core_web_lg`

`en_core_web_md` is recommended as it strikes a balance between accuracy and
download size. Initial start-up performance and memory usage is also impacted
by your choice of model. For a phone app where accuracy is prioritized, this
software could be adapted to run on a server where initial start-up cost
and memory cost would be negligible. (Likely with a much improved model as well)
Otherwise, a small, specialized model could be generated specifically for names.

## Usage
Run `python3 driver.py`

## Accuracy
Name recognition is only as good as the NER model behind it. That is why `driver.py`
allows the user to select a model from the three base models spaCy
has available. en_core_web_sm tends to have false positives,
but en_core_web_md and en_core_web_lg have 100% accuracy on the example dataset
(which is only three cards, more data is needed to actually assess the accuracy).

## Notes
### Choice of NLP library
spaCy was chosen as our NLP as opposed to NLTK or Core NLP due to two
reasons. First, spaCy is more intuitive to install and implement. Second,
spaCy is, [from their given benchmarks](https://spacy.io/usage/facts-figures#benchmarks)
, "the fastest syntactic parser in the world".

### Choice of language
Python was used for this challenge because of both its simplicity and its
ease of setup. Java was considered due to it being the native runtime of
Android, but not chosen because from the scope of the challenge,
I decided that ease of setup was the main priority.

### Telephone vs. Fax
The challenge is built such that there is a problem posed between telephone and
fax numbers. This implementation does attempt to naively exclude fax numbers
by excluding strings beginning with "Fax". In cases where business cards use
pictures instead of text to distinguish the two phone numbers, this solution fails.

A better solution could be to allow the user of the app to select which phone number
is the correct one. This solution could be extended to all info types, because
the main parser method (getContactInfo) is built to initially find all info matches.
It would be trivial to modify it such that it returns all of the possible matches
as a set of key,value pairs instead of a ContactInfo object. This would allow
outside implementation to choose which match is most appropriate.

### Inaccuracies in en_core_web_sm
The en_core_web_sm model incorrectly identifies "Software Developer"
as a name. This is masked by the fact that the true name comes before
"Software Developer" in example.txt. However, it is shown when viewing all matches.

The only way to correct this is to use a better model, such as en_core_web_md.

### Fragility of example.txt
The extraction of card data in example.txt is simple, it denotes
single business cards as blocks of text seperated by two newline (\n) characters.
Because of this, ensure that if `example.txt` is changed, that there are no leading newlines
at the end of the file. Otherwise, the program will not properly read the file.

### Licensing
   - spaCy: [The MIT License](https://github.com/explosion/spaCy/blob/master/LICENSE)
   - spaCy models: [CC BY-SA 3.0](https://spacy.io/models/en#en_core_web_sm)

## Examples
### Simple example
```
>> python3 driver.py

Select a spacy model:
        1. en_core_web_sm
        2. en_core_web_md
        3. en_core_web_lg
1
Would you like to time the parsing? (y/n)
n
Show all matches? (i.e., not just first found) (y/n)
n

Loading model...

=>

Name: John Doe
Phone: 4105551234
Email: john.doe@entegrasystems.com

Name: Jane Doe
Phone: 4105551234
Email: Jane.doe@acmetech.com

Name: Bob Smith
Phone: 17035551259
Email: bsmith@abctech.com
```

### Timed examples

#### Timed and showing all matches with model en_core_web_sm
```
>> python3 driver.py

Select a spacy model:
        1. en_core_web_sm
        2. en_core_web_md
        3. en_core_web_lg
1
Would you like to time the parsing? (y/n)
y
How many iterations (higher => more accurate, but slower)
        1. 10
        2. 100
        3. 250
3
Show all matches? (i.e., not just first found) (y/n)
y

Loading model...

=>

Timing, please wait...
        Card parsing took  0.03299933907162226 seconds on average over 250 iterations
- Matched names:  ['John Doe']
- Matched phone numbers:  ['4105551234']
- Matched email addresses ['john.doe@entegrasystems.com']
Name: John Doe
Phone: 4105551234
Email: john.doe@entegrasystems.com

Timing, please wait...
        Card parsing took  0.056581357824984836 seconds on average over 250 iterations
- Matched names:  ['Jane Doe']
- Matched phone numbers:  ['4105551234']
- Matched email addresses ['Jane.doe@acmetech.com']
Name: Jane Doe
Phone: 4105551234
Email: Jane.doe@acmetech.com

Timing, please wait...
        Card parsing took  0.0717529597735072 seconds on average over 250 iterations
- Matched names:  ['Bob Smith', 'Software Engineer']
- Matched phone numbers:  ['17035551259']
- Matched email addresses ['bsmith@abctech.com']
Name: Bob Smith
Phone: 17035551259
Email: bsmith@abctech.com
```
#### Timed and showing all matches with model en_core_web_md
```
>> python3 driver.py

Select a spacy model:
        1. en_core_web_sm
        2. en_core_web_md
        3. en_core_web_lg
2
Would you like to time the parsing? (y/n)
y
How many iterations (higher => more accurate, but slower)
        1. 10
        2. 100
        3. 250
3
Show all matches? (i.e., not just first found) (y/n)
y

Loading model...

=>

Timing, please wait...
        Card parsing took  0.03451846540676288 seconds on average over 250 iterations
- Matched names:  ['John Doe']
- Matched phone numbers:  ['4105551234']
- Matched email addresses ['john.doe@entegrasystems.com']
Name: John Doe
Phone: 4105551234
Email: john.doe@entegrasystems.com

Timing, please wait...
        Card parsing took  0.056735126486736745 seconds on average over 250 iterations
- Matched names:  ['Jane Doe']
- Matched phone numbers:  ['4105551234']
- Matched email addresses ['Jane.doe@acmetech.com']
Name: Jane Doe
Phone: 4105551234
Email: Jane.doe@acmetech.com

Timing, please wait...
        Card parsing took  0.07317037637579248 seconds on average over 250 iterations
- Matched names:  ['Bob Smith']
- Matched phone numbers:  ['17035551259']
- Matched email addresses ['bsmith@abctech.com']
Name: Bob Smith
Phone: 17035551259
Email: bsmith@abctech.com
```