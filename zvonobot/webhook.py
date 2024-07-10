import asyncio
import logging

import flask
from flask import Flask, request

import urllib.parse



app = Flask(__name__)

@app.route('/get_requests', methods=['POST'])
def get_web_hook():
    app.logger.info(f'{request}')

    if request.method == 'POST':
        name = request.stream.read().decode('utf-8')
        app.logger.info(f'{name=}')
        parse_data = urllib.parse.parse_qs(name)
        app.logger.info(f'{parse_data=}')
        telegram_id = int(parse_data.get('label', [''])[0])
    else:
        app.logger.critical('Ошибочка 403')
        flask.abort(403)

if __name__ == '__main__':
    app.run(debug=True)