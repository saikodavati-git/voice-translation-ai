import gradio as gr
import assemblyai as aai
import uuid
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from pathlib import Path


def voice(audio_file):

    # transcribe audio
    transcription_response = audio_transcription(audio_file)

    if transcription_response.status == aai.Transcriptstatus.error:
        raise gr.Error(transcription_response.error)
    else:
        text = transcription_response.text

        te_translation, hi_translation, fr_translation = text_translation(text)

        te_audi_path = text_to_speech(te_translation)
        hi_audi_path = text_to_speech(hi_translation)
        fr_audi_path = text_to_speech(fr_translation)

        te_path = Path(te_audi_path)
        hi_path = Path(hi_audi_path)
        fr_path = Path(fr_audi_path)

        return te_path, hi_path, fr_path


def audio_transcription(audio_file):

    aai.settings.api_key = "96b49346e938450eabff743df5cf6"

    transcriber = aai.Transcriber()
    transcription = transcriber.transcribe(audio_file)

    return transcription


def text_translation(text):

    translator_te = Translator(from_lang="en", to_lang="te")
    te_text = translator_te.translate(text)

    translator_hi = Translator(from_lang="en", to_lang="hi")
    hi_text = translator_hi.translate(text)

    translator_fr = Translator(from_lang="en", to_lang="fr")
    fr_text = translator_fr.translate(text)

    return te_text, hi_text, fr_text


def text_to_speech(text):
    client = ElevenLabs(
        api_key="sk_5f37b9d7c71f449cfca3ba7ec63bab236d8ee1c9b15ab7",
    )
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="A7VpD0eF3nBikfDPXj55",  # phanindra
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_multilingual_v2",  # use the turbo model for low latency
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.6,
            similarity_boost=1.0,
            style=0.5,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )
    # uncomment the line below to play the audio back
    # play(response)
    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"
    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    print(f"{save_file_path}: A new audio file was saved successfully!")
    # Return the path of the saved audio file
    return save_file_path


audio_input = gr.Audio(sources=["microphone"], type="filepath")

demo = gr.Interface(
    fn=voice,
    inputs=audio_input,
    outputs=[
        gr.Audio(label="Telugu"),
        gr.Audio(label="Hindi"),
        gr.Audio(label="French"),
    ],
)
if __name__ == "__main__":
    demo.launch()
