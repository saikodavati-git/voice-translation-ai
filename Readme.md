AI Voice Translator & Speech-to-Speech Converter

This project is an AI-powered voice translation application that converts spoken audio into multiple languages and generates corresponding speech outputs. It demonstrates a complete speech-to-speech pipeline, combining transcription, translation, and text-to-speech technologies into a single interactive system.

The application allows users to record audio through a microphone, transcribes the speech into text using AI, translates it into multiple languages, and then converts each translated text back into natural-sounding audio.

 Features:
Voice input using microphone
Speech-to-text transcription using AssemblyAI
Multi-language translation (Telugu, Hindi, French)
High-quality text-to-speech using ElevenLabs
Interactive UI built with Gradio

How It Works:

Voice Input → Speech Recognition → Text Translation → Speech Generation → Audio Output
User records audio via the interface
Audio is transcribed into text
Text is translated into selected languages
Each translated text is converted into speech
Final audio outputs are displayed in the UI

Tech Stack:
Python
Gradio
AssemblyAI (Speech-to-Text)
Translate Library (Text Translation)
ElevenLabs (Text-to-Speech)

How to Run:
Install dependencies:
pip install gradio assemblyai translate elevenlabs
Add API keys for AssemblyAI and ElevenLabs

Run the application:
python app.py
Open the local URL in your browser to use the app

