from flask import Flask, jsonify
import io
import zipfile
import base64
import requests
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

@app.route("/")
def hello_world():
    list_files = ['receip.jpg']

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for file_name in list_files:
            with open(file_name, "rb") as image_file:
                zip_file.writestr(file_name, image_file.read())

    encode_zip_string = base64.b64encode(zip_buffer.getvalue()).decode("utf-8")

    #CLIENT_ID = os.getenv('CLIENT_ID')
    #CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    #USERNAME = os.getenv('USERNAME')
    #API_KEY = os.getenv('API_KEY')

    CLIENT_ID='vrfA7J8C3OPCMktlMvHLjJASaPDVk4CKimzuOhW'
    CLIENT_SECRET='fWIwIRpnyHVh0a77uyCLsejKx2nh5zDUyoTNHH0EfYpJuSG6ucZTR4DSIHwnuhDbbB100JjclSmmKKsRc8LmNgAMc0xmvvCm9WYwLXYg8Y0dKy6tjwi9eCpeT4N4PJc3'
    USERNAME='kiprotichnickson0'
    API_KEY='e9775f05974eb12d6159ee8e92c33fd3'

    headers = {
            "User-Agent": "Python Veryfi-Python/3.0.0",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Client-Id": CLIENT_ID,
            "Authorization": f"apikey {USERNAME}:{API_KEY}"
            }
    api_url = "https://api.veryfi.com/api/v8/partner/documents"
    request_arguments = {
            "file_data": encode_zip_string,
            }
    _session = requests.Session()
    response = _session.request(
            "POST",
            url=api_url,
            headers=headers,
            data=json.dumps(request_arguments),
            )

    resp = response.json()
    return resp
    resp = resp['line_items']

    data = []
    for i in range(len(resp)):
        item = {
                'description': resp[i]['description'],
                "id":  resp[i]['id'],
                "price": resp[i]['price'],
                "quantity": resp[i]['quantity'],
                'total': resp[i]['total']
                }
        data.append(item)

    return data
        




if __name__ == '__main__':
    app.run()
