
from flask import Flask, request, Response, render_template
import os
from io import BytesIO
from gtts import gTTS
import base64


DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__, template_folder='david/templates', static_folder='david/static')

@app.route("/", methods=["GET", "POST"])
def home():

	if request.method == "GET":
		return render_template("index.html")
	elif request.method == "POST":
		try:
			input_text = request.form.get("input_text")
			lang = request.form.get("lang", DEFAULT_LANG)
			fp = BytesIO()
			gTTS(input_text,"com",lang).write_to_fp(fp)
			fp.seek(0)
			audio_base64 = base64.b64encode(fp.getvalue()).decode('utf-8')
			return render_template("index.html", audio=audio_base64)
		except Exception as e:
			return render_template("index.html", error=str(e))

if __name__ == '__main__':
    app.run('0.0.0.0', 80)
