from db2rest.renderer import Renderer, Response
import db2rest.helpers as helpers
from db2rest.exceptions import MethodNotAllowed


class RestAPI(object):

    def __init__(self, db_adapter, params):
        self.db_adapter = db_adapter
        self.params = params
        self.renderer = Renderer()
        self.views = dict((v.name, v) for v in views)

    def _create_response(self, request, row_id):
        response = None
        if row_id:
            msg = "Resource created"
            response = Response(msg, status="201")
            response.location = "/".join((request.path, str(row_id)))
        return response

    def post(self, request, response):
        view = self.views.get(self.params['view'])
        row_id = view(self.db_adapter, request, self.params).create()
        self._create_response(request, row_id)
        return self.renderer(view, request, row_id, response)

    def get(self, request, response):
        view = self.views.get(self.params['view'])
        data = view(self.db_adapter, request, self.params).get()
        return self.renderer(view, request, data)

    def delete(self):
        raise NotImplementedError("Not yet")

    def update(self):
        raise NotImplementedError("Not yet")


class View(object):

    def __init__(self,  db_adapter, req, params):
        self.db_adapter = db_adapter
        self.request = req
        self.params = params


class Table(View):

    name = 'Table'
    valid_methods = ['get', 'post']
    template_name = "Table"

    def _create(self):
        table_name = helpers.extract_table_name(self.request)
        values = self.request.values
        return self.db_adapter.add_row(table_name, values)

    def create_json(self):
        """Extracts the values from the json request and
        create the resource.
        """
        return self._create()

    def create_html(self):
        """Extract the values from the html request and
        create the resource.
         """
        return self._create()

    def __getattribute__(self, name):
        if name in ["create", "get"]:
            request = object.__getattribute__(self, 'request')
            ext = helpers.extract_file_ext(request)
            name = "_".join((name, ext))
        return object.__getattribute__(self, name)

    def _get(self):
        table = self.request.path[1:]
        headers = self.db_adapter.get_headers(table)
        rows = self.db_adapter.get_rows(table)
        return table, headers, rows

    def get_json(self):
        table, headers, rows = self._get()
        rows = [dict(zip(headers, row)) for row in rows]
        return {table: rows}

    def get_html(self):
        table, headers, rows = self._get()
        return dict(headers=headers, rows=rows, table=table)


class Tables(View):

    name = 'Tables'
    valid_methods = ['get']
    template_name = "Tables"

    def get(self):
        return dict(tables=self.db_adapter.get_tables())

    def create(self):
        raise MethodNotAllowed(description="This is a readonly view",
                               valid_methods=self.valid_methods,
                               method='post')


class Row(Table):
    name = 'Row'
    valid_methods = ['get', 'post', 'put', 'delete']
    template_name = "Table"

    def _get(self):
        table, row_id = helpers.extract_table_row_id(self.request.path)
        headers = self.db_adapter.get_headers(table)
        rows = self.db_adapter.get_row(table, row_id)
        return table, headers, rows


views = [Table, Tables, Row]
