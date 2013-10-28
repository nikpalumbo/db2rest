import werkzeug.exceptions as ex
from db2rest.helpers import is_json_request
from simplejson import JSONEncoder as encoder


class MethodNotAllowed(ex.MethodNotAllowed):

    def __init__(self, description, valid_methods, request, method):
        super(MethodNotAllowed, self).__init__(description=description,
                                               valid_methods=valid_methods)
        self.request = request
        self.method = method

    def get_body(self, environ=None):
        body = super(MethodNotAllowed, self).get_body(environ)
        if is_json_request(self.request):
            body = dict(detail="The method %s is not allowed"
                        % self.method.upper())
        return encoder().encode(body)

    def get_reponse(self):
        resp = super(MethodNotAllowed, self).get_response()
        resp.mimetype = self.request.accept_mimetypes.best
        return resp
