### --- Useful Libraries --- ###
import json

### --- REST API `routes` --- ###
from routes import users
users = users.Route()

### --- Flask for instantiating web service --- ###
from flask import Flask, Response
from flask import request as Request
app = Flask(__name__)

### --- ROUTE DETAILS --- ###
### Accessible via `http://<HOSTNAME>:5000/v1/users[/<optional, user id>]` (port defaults to 5000 for Flask)
### Available HTTP methods: `GET`, `POST`, `DELETE`
### Logic for the route is implemented in `routes/users.py`

@app.route('/v1/users', defaults={ 'user_id': None }, methods=['GET', 'POST'])
@app.route('/v1/users/<user_id>')
def route_users(user_id):
  # FYI: If HTTP Method is GET (equiv. fetch data, list info, etc)
  if Request.method == 'GET':
    result = users.get(user_id)
    if result == False:
      return send({
        'status':500,
        'reply': { 'code': 'SERVER_ERROR' }
      })
    else:
      return send({
        'status':200,
        'reply': { 'code': 'OK', 'output': result }
      })
  
  # FYI: If HTTP Method is POST (equiv. create new data, add new object, etc)
  elif Request.method == 'POST':
    data = json.loads(Request.data)
    result = users.post(data)
    if not result:
      return send({
        'status':500,
        'reply': { 'code': 'SERVER_ERROR' }
      })
    else:
      return send({
        'status':200,
        'reply': { 'code': 'OK', 'output': result }
      })
  
  # FYI: If HTTP Method is unrecognized
  else:
    return send({
      'status':404,
      'reply': { 'code': 'NOT_FOUND' }
    })


### --- HELPER: Send Reply --- ###
### Function for constructing response to HTTP Request
def send(resp):
  return Response(
    json.dumps(resp.get('reply')),
    status=resp.get('status'),
    mimetype='application/json')