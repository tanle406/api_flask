from gtts import gTTS
import os
import base64

def mp3_to_base64(mytext, language):

    audio = gTTS(text=mytext, lang=language, slow=False)
    audio.save("example.mp3")

    with open("example.mp3", "rb") as mp3_file:
        encoded_string = base64.b64encode(mp3_file.read())

    os.remove("example.mp3")

    return encoded_string
