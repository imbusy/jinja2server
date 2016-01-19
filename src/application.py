from wsgiref.util import request_uri
from urllib.parse import urlparse
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

templates = Environment(loader=FileSystemLoader('/home/web/templates'), auto_reload=True)

def application(env, start_response):
  URI = request_uri(env)
  parsed = urlparse(URI)
  path = parsed.path
  if path == '/':
    path = 'index.html'
  path = path.replace('..', '')

  # content-type, binary
  types = {
    'htm': ['text/html', False],
    'html': ['text/html', False],
    'css': ['text/css', False],
    'jpg': ['image/jpeg', True],
    'jpeg': ['image/jpeg', True],
    'png': ['image/png', True],
    'json': ['application/json', False],
    'txt': ['text/plain', False]
  }

  content_type = types.get(path.split('.')[-1], ['application/octet-stream', True])
  try:
    if not content_type[1]:
      result = templates.get_template(path).render().encode('utf-8')
    else:
      result = open('/home/web/templates/'+path,'rb').read()
  except TemplateNotFound:
    start_response('404 Not Found', [('Content-Type','text/plain')])  
    return [b'404 Not Found']
  start_response('200 OK', [('Content-Type',content_type[0])])

  return [result]
