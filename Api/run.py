"""
Entry point of the app
Runs the app in specified exported mode
"""
import os # allow workings of underlieing os

# import the APP used to instanciate flask
from api import APP

# run the app

if __name__ == '__main__':
    APP.run()