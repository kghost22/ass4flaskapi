import flask
from flask import request, jsonify
from flask_cors import CORS 

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

covidcases = [
    {'id': 0,
     'country': 'Ghana',
     'total_cases': '311',
     'recoveries': '45',
     'active_cases': '8',
     'total_deaths': '1'
     },
    {'id': 1,
     'country': 'Nigeria',
     'total_cases': '311',
     'recoveries': '45',
     'active_cases': '8',
     'total_deaths': '1'
     },
   {'id': 2,
     'country': 'Benin',
     'total_cases': '333',
     'recoveries': '23',
     'active_cases': '34',
     'total_deaths': '19'
     }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Covid tracker</h1>
<p>A covid application to track their cases</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/covid/all', methods=['GET'])
def api_all():
    return jsonify(covidcases)

app.run()