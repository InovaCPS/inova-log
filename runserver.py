#!/usr/bin/env python
#
#   This script will run the main application file in debug mode.
#
#   author: Michael Gruber

from sys import path

path.append("src/main/python")

from webapp import app

app.run(host='0.0.0.0', debug=True, port=8080)
