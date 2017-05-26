# -*- encoding=UTF-8 -*-

from mystagram import app

@app.route('/')
def index():
    return 'Hello'

