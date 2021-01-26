from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesecretkey'

apps = {
    "1": "python",
    "2": "java"
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/api/v1/app/')
@token_required
def findApp():
    appid = request.args.get('appid')
    if appid in apps:
        return jsonify(apps[appid])
    return jsonify({'message': 'No app id found'})

@app.route('/api/v1/app/', methods=['POST'])
@token_required
def addApp():
    try:
        req_data = request.get_json()
        app = req_data['app']
        name = req_data['name']
        version = req_data['version']
    except:
        return jsonify({'message': 'Data is invalid!'}), 403

    print('Here\'s your post data : ' + app + ' - ' + name + ' - ' + version)
    return make_response('successful',200)

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if auth and auth.password == 'secret':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=150)}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token' : token})

    return make_response('Could not verify!', 404, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(port=8083,debug=True)
