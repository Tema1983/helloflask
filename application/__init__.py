from flask import Flask
app = Flask(__name__)

import application.views
import application.secondView
import application.commandView