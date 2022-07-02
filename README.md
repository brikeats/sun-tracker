# Sun Position

An app for AR display of sun's trajectory.

## Quickstart

* Create python environment: `conda create -n sun -y python=3.9 && conda activate sun`
* Install dependencies: `pip install requirements.txt`
* Generate self-signed certificat: `openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`. This is necessary even for development because browsers only allow camera access to https pages.
* Start server: `gunicorn -b 0.0.0.0:5000 app:app --certfile cert.pem --keyfile key.pem --capture-output --log-level debug`. For some reason flask's development server wasn't consistently working, but gunicorn seems okay.

View in browser: https://<your-dev-machine-ip>:5000. Because it's a self-signed certificate, browsers will produce a big "Warning: Insecure connection" page. In Chrome, you can click "Advanced" and then "Proceed to https://<your-dev-machine-ip>:5000" to get to the page. You'll then be asked for camera permissions.

------

`python sunpos.py  # prints sun coordinates at sunset`

## Credits

[HTML5 Video stuff from here](https://demo.kasperkamperman.com/mobilecamtemplate/)