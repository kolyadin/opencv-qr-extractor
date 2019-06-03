from flask import Flask, Response, jsonify
from gevent.pywsgi import WSGIServer
from flask import request
import extractor
import tempfile
import os
import cv2
import json
import optimizer

app = Flask(__name__)

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_data()

    path = os.path.join(tempfile.mkdtemp(), 'decode')

    with open(path, "wb")  as outfile:
        outfile.write(data)

    src = cv2.imread(path)
    os.remove(path)

    qrString = extractor.decode(src)

    if qrString:
        data = {}
        data['qrString'] = qrString.strip("\r\n")

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )

        response.headers['X-Smart-Algorithms'] = 'MISS'

        return response
    else:
        qrString = optimizer.zoomer(src)

        if qrString:
            data = {}
            data['qrString'] = qrString.strip("\r\n")

            response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )

            response.headers['X-Smart-Algorithms'] = 'HIT'

            return response
        else:
            return Response(status=400)


if __name__ == '__main__':
    # Production
    print("Running web server")
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
