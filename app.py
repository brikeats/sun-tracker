import os
from flask import Flask, send_from_directory, render_template


app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':

    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'))
