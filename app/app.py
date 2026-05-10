from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Jordi, Chris, en serio vayanse directito a la... los tqm, ah y corriendo en puerto 5000"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)