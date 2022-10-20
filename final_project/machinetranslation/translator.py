"""
Translator service
"""
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2018-05-01'
EN_FR = 'en-fr'
FR_EN = 'fr-en'

def get_translation(model_id, text):
    """
    Since IAMAuthenticator is throwing a TLS Version error I had to
    implement the translation service via REST
    """
    if text is None or len(text) == 0:
        return None
    if model_id is None or len(model_id) == 0:
        return None
    data = json.dumps({
        'text': [text],
        'model_id': model_id
    })
    response = requests.post(
        auth=('apikey', API_KEY),
        headers={'Content-Type': 'application/json'},
        data=data,
        url=URL+'/v3/translate?version='+VERSION
    )
    response = response.content.decode('utf8').replace("'", '"')
    content = json.loads(response)
    if 'translations' not in content:
        return None
    if len(content['translations']) == 0:
        return None
    translation = content['translations'][0]

    return translation['translation']

def english_to_french(text):
    """
    Translates English to French
    """
    return get_translation(EN_FR, text)

def french_to_english(text):
    """
    Translates English to French
    """
    return get_translation(FR_EN, text)
