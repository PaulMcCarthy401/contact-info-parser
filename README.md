# contact-info-parser
A business card info parser for arbitrary contact info.

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

4. Install spacy
```
pip install -U spacy
```
Note: Windows users will need to install a version of the Visual C++ Build Tools and the Windows 10 SDK
  Python 3.4 -> Visual Studio 2010
  Python 3.5+ -> Visual Studio 2015

## Accuracy
Name recognition is only as good as the NER model behind it. That is why `driver.py`
allows the user to select a model. en_core_web_sm tends to have false positives,
but en_core_web_md and en_core_web_lg have 100% accuracy on the example dataset.
(Which is only three cards, more data is needed to accurately assess the performance)

## Example
```
(env) D:\code\contact-info-parser> python driver.py

Select a spacy model:
        1. en_core_web_sm
        2. en_core_web_md
        3. en_core_web_lg
1

=>

Name: John Doe
Phone: 4105551234
Email: john.doe@entegrasystems.com

Name: Jane Doe
Phone: 4105554321
Email: Jane.doe@acmetech.com

Name: Software Engineer
Phone: 17035551200
Email: bsmith@abctech.com
```