from definitions import ROOT_DIR
import requests


audio_file_to_send = ROOT_DIR.joinpath("testing_audio_files/1615792075476.wav")
csv_file_to_send = ROOT_DIR.joinpath("testing_audio_files/build_Noise-Capture-Form_1614927723.csv")


def send_file(file_to_send, file_type):
    with open(file_to_send, 'rb') as f:
        r = requests.post(f'http://127.0.0.1:5000/{file_type}', files={file_type: f})
        print(r.text)


if __name__ == '__main__':
    send_file(csv_file_to_send, 'csv')
