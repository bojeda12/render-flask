from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Modificacion para nuestro railway, todo funciona!!!"
if __name__ == "__main__":
    app.run()
