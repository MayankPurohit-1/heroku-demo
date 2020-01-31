from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''<form action=# method= "POST">
    Username:<input type=text name="username">
    Password:<input type=password name="password">
    </form>
    '''



