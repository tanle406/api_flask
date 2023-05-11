from flask import Flask, request
from lib.ask_for_gpt import ask_chatgpt
from lib.text_to_speech import mp3_to_base64

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    my_text = data['text']
    language = data['language']
    try:
        answer = ask_chatgpt(my_text)
        mp3 = mp3_to_base64(answer, language)
    except Exception as e:
        print("Error asking ChatGPT", e)
    print(mp3)
    return mp3
    # return my_text + '\n' + language


if __name__ == '__main__':
    app.run()
