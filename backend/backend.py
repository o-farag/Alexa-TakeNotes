from flask import Flask, jsonify, request
from flask_cors import CORS
from transcribe import upload_file_to_s3
import helpers
import boto3
import text_to_img
import secrets

app = Flask(__name__)
CORS(app)

@app.route('/api/go', methods=['POST'])
def go():
    files = request.get_json()

    random_bytes = secrets.token_bytes(10)

    s3_client = boto3.client('s3')
    if ("recording" in files):
        recording = files["recording"]
        recordingName = '/Users/jessicahe/Documents/UofT/Hackathon/demo/' + recording
        upload_file_to_s3('h12324bucket', recordingName, s3_client)
    if ("slides" in files):
        slides = files["slides"]
        slidesName = '/Users/jessicahe/Documents/UofT/Hackathon/demo/' + slides
        upload_file_to_s3('h12324bucket', slidesName, s3_client)
    #if ("text" in files):
        #text = files["text"]
        #text.name = text.name + random_bytes
        #upload_file_to_s3('h12324bucket', text, s3_client)

    return "Done", 201

@app.route('/api/get')
def get():
    # This could be any data retrieval or processing logic
    data = {"message": "Hello from Flask!"}
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000)
