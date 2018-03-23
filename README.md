# contact-info-parser
A business card info parser for arbitrary contact info, built with Python 3 and spaCy.

## Installation
1. Pull down the Github repo
```
git clone https://github.com/PaulMcCarthy401/contact-info-parser.git
```
2. Set up a python virtual environment
```
python -m venv env
```
3. Switch into python environment
   - Windows `env\Scripts\activate`
   - Linux/Mac `source env/bin/activate`

4. Install dependencies
```
pip install -r requirements.txt
```
Note: Before installing dependencies, Windows users will need to install
a version of the Visual C++ Build Tools and the Windows 10 SDK.
More info about compiler dependencies due to spaCy
can be found [here](https://spacy.io/usage/#source-windows)

  - Python 3.4  -> Visual Studio 2010
  - Python 3.5+ -> Visual Studio 2015

Generic installation instructions can be found [here](https://spacy.io/usage/#pip)

5. Choose a model
   - Small:  `python -m spacy download en_core_web_sm`
   - Medium: `python -m spacy download en_core_web_md`
   - Large:  `python -m spacy download en_core_web_lg`

`en_core_web_md` is recommended as it strikes a balance between accuracy and
download size. Initial start-up performance and memory usage is also impacted
by your choice of model. For a phone app where accuracy is prioritized, this
software would be adapted to run on a server where initial start-up cost
and memory cost would be negligible. (Likely with a much improved model as well)

## Accuracy
Name recognition is only as good as the NER model behind it. That is why `driver.py`
allows the user to select a model from the three base models spaCy
has available. en_core_web_sm tends to have false positives,
but en_core_web_md and en_core_web_lg have 100% accuracy on the example dataset
(which is only three cards, more data is needed to actually assess the accuracy).

## Example
```
>> python driver.py

Select a spacy model:
        1. en_core_web_sm
        2. en_core_web_md
        3. en_core_web_lg
2

=>

Name: John Doe
Phone: 4105551234
Email: john.doe@entegrasystems.com

Name: Jane Doe
Phone: 4105554321
Email: Jane.doe@acmetech.com

Name: Bob Smith
Phone: 17035551200
Email: bsmith@abctech.com
```