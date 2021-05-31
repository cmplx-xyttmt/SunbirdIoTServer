from app import app
from flask import request
from werkzeug.utils import secure_filename
from upload_to_s3 import upload_to_aws
from datetime import datetime


def allowed_audio_file(filename: str):
    return filename.lower().endswith(('.wav', '.mp3'))


def allowed_csv_file(filename: str):
    return filename.lower().endswith('.csv')


@app.route("/audio", methods=['POST'])
def upload_audio():
    try:
        file = request.files['audio']
        print(file.content_type)
        if file and allowed_audio_file(file.filename):
            filename = secure_filename(file.filename)
            print(type(file))
            upload_to_aws(file, 'sunbird-noise-storage', f'audio-files/{datetime.now()}-{filename}')
            return f"Successfully uploaded {filename}", 200
    except Exception as e:
        print(e)
        return "Failed to upload file", 422


@app.route("/csv", methods=['POST'])
def upload_csv():
    try:
        file = request.files['csv']
        print(file.content_type)
        if file and allowed_csv_file(file.filename):
            filename = secure_filename(file.filename)
            upload_to_aws(file, 'sunbird-noise-storage', f'csv-files/{filename}')
            return f"Successfully uploaded {filename}", 200
    except Exception as e:
        print(e)
        return "Failed to upload file", 422


@app.route('/')
@app.route('/index')
def index():
    return {'hello': 'world'}
