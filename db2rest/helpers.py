def extract_file_ext(request):
    """
    Extracts file extension either from a request, or enviroment.
    """
    if isinstance(request, basestring):
        mimetype = request
    else:
        mimetype = request.accept_mimetypes.best
    return mimetype.split('/')[1]


def extract_table_name(request):
    """Extracts the table name from the request.path.
    """
    return request.path.split("/")[1]


def is_json_request(request):
    """Return true is the best accept mimetype is json.
    """
    return extract_file_ext(request) == 'json'
