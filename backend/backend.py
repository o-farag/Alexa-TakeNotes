from flask import Flask, jsonify
from flask_cors import CORS
import helpers

app = Flask(__name__)
CORS(app)

@app.route('/api/go')
def go():
    
    #Depending on state, use different services
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

@app.route('/api/get')
def get():
    # This could be any data retrieval or processing logic
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
