from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    players = ["salwa", "tamer", "mohammad"]
    player1="einav"
    return render_template("index.html",player1=player1,players=players,likes_same_sport=True)

 
if __name__ == '__main__':
    app.run(debug=True)