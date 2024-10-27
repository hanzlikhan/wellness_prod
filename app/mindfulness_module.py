# mindfulness_module.py
from gtts import gTTS

def get_mindfulness_text():
    return "Take a deep breath, focus on the present, and reflect on a positive moment from today."

def generate_audio_from_text(text, filename="assets/mindfulness_audio_generated.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename
