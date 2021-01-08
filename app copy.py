from flask import Flask, render_template, send_file, request

app = Flask(__name__)

links = {
	"GitHub": "https://github.com/02AngelaChang",
	"LinkedIn":"https://www.linkedin.com/in/angela-chang-1341581b8",
}

@app.route('/', methods=["GET", "POST"])
def index():

	if request.method == "POST" : #post request
		 with open("Resume_Angela_Chang.pdf", "rb") as f:
			return send_file(f, attachment_filename="Angela's_Resume.pdf", as_attachment=True)
    
    	else: #get request
    		return render_template("index.html", links=links)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
