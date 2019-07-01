import json 

class Route:
  def __init__(self, users=[]):
    self._users = users
    self._counter = 0

  ### Functionalities:
  ### - Get list of users and their details
  ### - Get a specific user and its details
  def get(self, id=None):
    if not id:
      return self._users
    else:
      for u in self._users:
        if u.get('id') == int(id):
          return u
      return False

  ### Functionalities:
  ### - Create new user
  def post(self, data):
    self._counter = self._counter + 1
    user_data = { 'id': self._counter, 'data': data }
    self._users.append(user_data)
    return True

  def delete(self):
    return True
  
  def put(self):
    return True
