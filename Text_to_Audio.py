from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'pt'
msg = 'Seu texto aqui.'
sp = gTTS(text= msg, lang=language, slow=False)

sp.save(audio)
playsound(audio)