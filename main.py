from flask import Flask, request, send_file
from gtts import gTTS

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get('text')
    lang = data.get('lang', 'en')
    if not text:
        return {'error': 'Text required'}, 400

    tts = gTTS(text=text, lang=lang)
    filename = 'output.mp3'
    tts.save(filename)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
