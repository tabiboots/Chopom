import sys
print(sys.executable)

import sounddevice as sd

# List all audio devices explicitly
print(sd.query_devices())

# Choose your microphone explicitly by its index number
mic_index = 3  # <-- Adjust this clearly based on output above

duration = 5  # seconds
sample_rate = 16000

print("🎙️ Recording...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, device=mic_index)
sd.wait()
print("Recording finished explicitly.")

# Save explicitly to test audio file
from scipy.io.wavfile import write
write("test_audio.wav", sample_rate, audio)
print("✅ Saved explicitly as test_audio.wav.")