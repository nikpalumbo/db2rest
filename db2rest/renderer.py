from werkzeug.wrappers import Response
from jinja2 import Environment, FileSystemLoader
from simplejson import JSONEncoder as encoder
import os


class Renderer(object):

    extension_accepted = ['html', 'json', 'xml']

    def __init__(self):
        self.template_path = os.path.join(os.path.dirname(__file__),
                                          'templates')
        loader = FileSystemLoader(self.template_path)
        self.jinja_env = Environment(loader=loader, autoescape=True)

    def __call__(self, template, req, data):
        return self.render_template(template, data, req.accept_mimetypes.best)

    def _render(self, data, file_ext, template_path):
        if file_ext == 'json':
            res = encoder().encode
        else:
            t = self.jinja_env.get_template(template_path)
            res = t.render
        return res

    def render_template(self, template_name, data, mimetype):
        file_ext = mimetype.split('/')[1]
        #To avoid rendering some unknown file
        if not file_ext in self.extension_accepted:
            return

        template_path = "".join((template_name, '.', file_ext))
        render = self._render(data, file_ext, template_path)
        return Response(render(data),  mimetype=mimetype)
