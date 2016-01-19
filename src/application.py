from collections import namedtuple
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

  FileContent = namedtuple('FileContent', ['content_type', 'binary'])
  # content-type, binary
  extensions = {
    'htm': FileContent('text/html', False),
    'html': FileContent('text/html', False),
    'css': FileContent('text/css', False),
    'jpg': FileContent('image/jpeg', True),
    'jpeg': FileContent('image/jpeg', True),
    'png': FileContent('image/png', True),
    'json': FileContent('application/json', False),
    'txt': FileContent('text/plain', False)
  }

  file_content = extensions.get(path.split('.')[-1], FileContent('application/octet-stream', True))
  try:
    if not file_content.binary:
      result = templates.get_template(path).render().encode('utf-8')
    else:
      result = open('/home/web/templates/'+path,'rb').read()
  except TemplateNotFound:
    start_response('404 Not Found', [('Content-Type','text/plain')])  
    return [b'404 Not Found']
  start_response('200 OK', [('Content-Type',file_content.content_type)])

  return [result]
