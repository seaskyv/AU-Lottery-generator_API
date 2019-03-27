import mylogger
import flask
from flask import request, jsonify
import lotteryGenerator
import yaml
import os
import io

# Load config from yaml file
with open("./config.yaml", 'r') as readConfig:
    try:
        config = yaml.load(readConfig)
        # print(config)
    except yaml.YAMLError as err:
        exit(err)

myLogging = mylogger.myLogger(config["Logger"]["logFileName"],config["Logger"]["maxLogFileSizeMB"],config["Logger"]["logLevel"],config["Logger"]["maxLogRotate"])

myLogging.info("API started")
# print(__name__)


app = flask.Flask(__name__)
app.config["DEBUG"] = config["Flask"]["Debug"]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>API for Lottery number Generator</h1>'''

@app.route('/api', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'game' in request.args:
        game = request.args['game']
    else:
        myLogging.warning("No game field provided.")
        return "<h1>400(Bad Request) :</h1><p>No game field provided. Please specify an game.</p>"
    if 'magic' in request.args:
        magic = int(request.args['magic'])
    else:
        myLogging.warning("No magic number field provided.")
        return "<h1>400(Bad Request) :</h1><p>No magic number field provided. Please specify an magic.</p>"
    if 'num' in request.args:
        num = int(request.args['num'])
    else:
        myLogging.warning("No number of games field provided.")
        return "<h1>400(Bad Request) :</h1><p>No number of games field provided. Please specify an magic.</p>"
    if 'system' in request.args:
        system = int(request.args['system'])
    else:
        myLogging.warning("No system of games field provided.")
        return "<h1>400(Bad Request) :</h1><p>No system of games field provided. Please specify an num.</p>"

    # Generate numbers
    myPlay = lotteryGenerator.PlayGame(game,magic,num,system)
    result = myPlay.callGames()
    #myLogging.info(result)
    #print(result) 

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if "PORT" in os.environ:
    portNum = os.environ["PORT"]
    print(portNum)
else:
    portNum = config["Server"]["portNumber"]
try:
    if 1 <= int(portNum) <= 65535:
        app.run(host='0.0.0.0', port= portNum)
    else:
        raise ValueError
except ValueError:
    print("This is NOT a VALID port number.")
    myLogging.fatal(portNum + " is NOT a VALID port number.")
    exit(1)

