from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
import requests
from app.models import db, Word
from app.words.forms import WordForm
import re

words_blueprint = Blueprint('words', __name__)

def clean_text(text):
    # Remove formatting markers
    text = re.sub(r'{[^}]+}', '', text)
    return text

def extract_dt_sn(data):
    dt_sn_pairs = []

    def traverse(data, current_sn=None, level=1):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'sn':
                    current_sn = value
                elif key == 'dt' and current_sn is not None:
                    for dt_item in value:
                        if isinstance(dt_item, list) and dt_item[0] == 'text':
                            clean_dt = clean_text(dt_item[1])
                            dt_sn_pairs.append((f"{level}-{current_sn}", clean_dt))
                else:
                    traverse(value, current_sn, level)
        elif isinstance(data, list):
            for item in data:
                traverse(item, current_sn, level+1)

    traverse(data)
    return dt_sn_pairs

def get_word_definition(word):
    api_key = current_app.config['MW_API_KEY']
    url = f"{current_app.config['MW_API_BASE_URL']}/{word}?key={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        return None, None, None

    data = response.json()

    if not data or not isinstance(data, list):
        return None, None, None  # Return None if the data is invalid

    word_data = data[0]  # Extract the first entry which contains the word data

    # Extract definitions
    dt_sn_pairs = extract_dt_sn(word_data)
    definitions = [(sn, dt) for sn, dt in dt_sn_pairs]

    # Extract pronunciations
    pronunciations = get_pronunciations(word_data)
    print(pronunciations)
    # Extract audio pronunciation URL
    audio_url = get_audio_pronunciation(word_data)

    return definitions, pronunciations, audio_url


def get_pronunciations(data):
    pronunciations = []
    if 'hwi' in data and 'prs' in data['hwi']:
        for pr in data['hwi']['prs']:
            if 'mw' in pr:
                pronunciations.append(pr['mw'])
    return pronunciations

def get_audio_pronunciation(data):
    # Extract the audio pronunciation URL from the API response
    if 'hwi' in data and 'prs' in data['hwi']:
        sound_name = data['hwi']['prs'][0]['sound']['audio']
        if sound_name:
            subdirectory = sound_name[:1] if sound_name[0].isalpha() else 'number'
            audio_url = f'https://media.merriam-webster.com/audio/prons/en/us/mp3/{subdirectory}/{sound_name}.mp3'
            return audio_url
    return "Audio pronunciation not available."

@words_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    # Handle the word search form submission
    form = WordForm()
    if form.validate_on_submit():
        word = form.word.data
        print(f"Searching for word: {word}") #debugging
        return redirect(url_for('words.results', word=word))
    return render_template('home.html', form=form)

@words_blueprint.route('/results/<word>')
def results(word):
    definitions, pronunciations, audio_url = get_word_definition(word)
    if definitions:
        return render_template('results.html', word=word, definitions=definitions, pronunciations=pronunciations, audio_url=audio_url)
    else:
        flash(f'No definition found for "{word}".')
        return redirect(url_for('words.search'))
    