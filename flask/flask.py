from flask import flask,render_template ,jsonify
from random import sample

app = Flask(__name___)

@app.route("/")
def index();
    return render_template('chart.html')

@app.route("/data")
def data();
 return jsonify('results':sample(range(1,10),5)))

if __name__ == '__main__':
app.run(debug =True)