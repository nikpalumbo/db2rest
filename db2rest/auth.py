from werkzeug.wrappers import Response


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'


def authenticate():
    """Sends a 401 response that enables basic auth.
    """
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def is_authenticated(request):
    """Verify wether the request is authorized or not.
    """
    auth = request.authorization
    return auth and check_auth(auth.username, auth.password)
