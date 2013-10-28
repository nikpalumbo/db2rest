import werkzeug.exceptions as ex
from db2rest.helpers import is_json_request
from simplejson import JSONEncoder as encoder


class HTTPExceptionMixin(ex.HTTPException):

    def get_response(self, environ):
        resp = super(HTTPExceptionMixin, self).get_response(environ)
        if is_json_request(environ.get('HTTP_ACCEPT')):
            resp.mimetype = environ['HTTP_ACCEPT']
        return resp

    def get_body(self, environ=None):
        body = super(HTTPExceptionMixin, self).get_body(environ)
        if is_json_request(environ.get('HTTP_ACCEPT')):
            body = dict(detail=self.body_message)
            body = encoder().encode(body)
        return body

    @property
    def body_message(self):
        raise NotImplemented("""The subclass is repsonsibile
                                to implemet this method""")


class MethodNotAllowed(ex.MethodNotAllowed, HTTPExceptionMixin):

    def __init__(self, description, valid_methods, request, method):
        super(MethodNotAllowed, self).__init__(description=description,
                                               valid_methods=valid_methods)
        self.request = request
        self.method = method

    @property
    def body_message(self):
        return "The method %s is not allowed" % self.method.upper()


    #def get_reponse(self):
    #    resp = super(MethodNotAllowed, self).get_response()
    #    resp.mimetype = self.request.accept_mimetypes.best
    #    return resp


class NotFound(ex.NotFound, HTTPExceptionMixin):

    @property
    def body_message(self):
        return "Resource Not Found"