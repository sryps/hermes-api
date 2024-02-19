from flask import Flask, request
from hermes import *

app = Flask(__name__)


# Route to handle GET requests for variables
@app.route('/hermes', methods=['GET'])
def hermes():
    chain = request.args.get('chain')
    channel = request.args.get('channel')
    
    if chain and channel is not None:
        resp = runHermes(chain,channel)
        return resp
    err = {}
    err['error'] = "add chain and channel"
    return err

if __name__ == '__main__':
    import logging
    logging.basicConfig(filename='error.log',level=logging.DEBUG)

    app.run(debug=True)
