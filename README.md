# SpeakPeak Dictionary

SpeakPeak Dictionary is a web application that allows users to search for word definitions and pronunciations. This application uses the Merriam-Webster API to fetch word data, including definitions and audio pronunciations.

## Deployment

Check out the live application [here](https://speakpeak.onrender.com/words/search).

## Features

- **Search for word definitions and pronunciations**
- Displays definitions with corresponding sense numbers
- Plays audio pronunciation for searched words
- Responsive and user-friendly interface

## Technologies Used

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: Jinja2, HTML5, CSS3, JavaScript, Bootstrap
- **API**: Merriam-Webster API

## Goal

To provide users with a web application where they can search for word definitions as well as hear and see their pronunciations.

## Prerequisites

All prerequisites and dependencies can be found in the `requirements.txt` file.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/speakpeak-dictionary.git
   cd speakpeak-dictionary

2. **Set up a virtual environment**

   ```sh
   python3 -m venv venv
   source venv/bin/activate 
 
3. **Install dependencies**
   
   ```sh
   pip install -r requirements.txt

4. **Set up environment variables**

   ```sh
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgresql:///speakpeak
   TEST_DATABASE_URL=postgresql:///speakpeak_test
   MW_API_KEY=your_merriam_webster_api_key
   MW_API_BASE_URL=https://www.dictionaryapi.com/api/v3/references/collegiate/json/

5. **Set up the database**

   ```sh
   createdb speakpeak
   flask db upgrade

6. **Run the application**

   ```sh
   flask run