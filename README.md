# Sun Position

An app for AR display of sun's trajectory.

## Quickstart

`conda create -n sun -y python=3.9 && conda activate sun`

`pip install requirements.txt`

`export FLASK_APP=app`

`export FLASK_ENV=development  # only for local testing; NOT for real deployment`

`flask run --host=0.0.0.0`

[View in browser](http://127.0.0.1:5000/)

------

`python sunpos.py  # prints sun coordinates at sunset`