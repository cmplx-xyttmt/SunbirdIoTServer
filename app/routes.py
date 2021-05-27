from app import app
from flask import jsonify, request
from werkzeug.utils import secure_filename
from definitions import FILE_UPLOAD_DIR


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
            file.save(FILE_UPLOAD_DIR.joinpath(filename))
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
            file.save(FILE_UPLOAD_DIR.joinpath(filename))
            return f"Successfully uploaded {filename}", 200
    except Exception as e:
        print(e)
        return "Failed to upload file", 422


@app.route('/')
@app.route('/index')
def index():
    return {'hello': 'world'}
