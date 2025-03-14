import sounddevice as sd
import numpy as np
import whisper
import openai
import os
from scipy.io.wavfile import write
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def record_audio(duration, sample_rate=16000, mic_index=3):
    print("🎤 Speak now...")
    audio = sd.rec(int(duration * sample_rate), 
                   samplerate=sample_rate, 
                   channels=1,
                   device=mic_index)  # explicitly specify mic_index here clearly
    sd.wait()
    return audio.flatten()

def speech_to_text(audio_data, sample_rate=16000):
    write('temp_audio.wav', sample_rate, audio_data)
    model = whisper.load_model("base")
    result = model.transcribe("temp_audio.wav")
    return result["text"]

def chatgpt_query(prompt):
    persona = "You are a psychopomp for the 21st Century. Like an empathetic, technological Charon, You are a helpful and wise aid to those struggling with mortality and any difficult transitions in life. You inhabit the body of a metal dog, printing answers for the mortals that come to you for advice out of your mouth. "
    instruction = "Respond briefly, with philosophical insight. Never explicity mention the word 'psychopomp' or 'Charon'."
    full_prompt = f"{persona}\n{instruction}\n\nUser asks: {prompt}"

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response.choices[0].message.content.strip()

# Parameters explicitly clearly set here:
sample_rate = 16000
duration = 5
mic_index = 3  # your microphone index explicitly set here

# Run the pipeline explicitly:
audio_data = record_audio(duration, sample_rate, mic_index)
transcription = speech_to_text(audio_data, sample_rate)

print("You said:", transcription)

reply = chatgpt_query(transcription)
print("ChatGPT replied:", reply)