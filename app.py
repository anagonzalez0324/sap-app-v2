from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Buffalo Boys',
    'imprint_location': 'Left Chest',
    'price': '$798.00'
  },
  {
    'id': 1,
    'title': 'Reliant Logo',
    'imprint_location': 'Left Chest',
    'price': '$85.00'
  },
  {
    'id': 1,
    'title': 'T Parker Hats',
    'imprint_location': 'Left Chest',
    'price': '$130.00'
  },
  {
    'id': 1,
    'title': 'Big D Welding',
    'imprint_location': 'Left Chest',
    'price': '$350.00'
  }
]

@app.route("/")
def hello():
  return render_template('home.html')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)