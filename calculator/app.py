"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, jsonify
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/add/<int:x>/<int:y>', methods=['GET'])
def add(x,y):
    result = {'result': x+y,  'from': 'Python services' }
    return jsonify(result)

if __name__ == '__main__':
    import os
    
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8084'))
    except ValueError:
        PORT = 8084
    app.run(host='0.0.0.0', port=PORT)
