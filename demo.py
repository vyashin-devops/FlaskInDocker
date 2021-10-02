from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "FLASK2DOCKER CI/CD IS SUCCESSFULL 15:22"


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)
