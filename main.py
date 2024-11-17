from flask import Flask, request, Response
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def proxy(path):
    target_url = request.args.get('url')
    if not target_url:
        return Response("Missing 'url' parameter", status=400)

    try:
        headers = {key: value for key, value in request.headers if key.lower() != 'host'}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        method = request.method
        data = request.get_data()

        response = requests.request(
            method=method,
            url=target_url,
            headers=headers,
            data=data,
            params=request.args,
            stream=False  # Disable streaming
        )

        return Response(
            str(response.status_code),  # Only return HTTP status code
            status=200
        )

    except requests.exceptions.RequestException as e:
        return Response("500", status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8989)
