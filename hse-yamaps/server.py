from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

import json
import os

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
    # Send response status code
    self.send_response(200)
    # Send headers
    self.send_header('Content-type','application/json')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
        
    params = parse_qs(urlparse(self.path).query)

    try:
        f = open(os.getcwd() + '/' + 'cords.txt', 'r')
        data={}
        data['type'] = "FeatureCollection"
        data['features'] = []
        for index, line in enumerate(f):
            t = line.split(' ')
            t[-1] = t[-1].replace('\n','')
            if t[-1] == 'Point':
                data['features'].append({
                    'type': 'Feature',
                    'id': index,
                    'geometry': {
                        'coordinates': [t[0], t[1]],
                        'type': 'Point'
                    },
                    'properties': {
                    'balloonContent': 'Содержимое балуна',
                    'clusterCaption': 'Еще одна метка',
                    'hintContent': 'Текст подсказки'
                    }
                })
                
            if t[-1] == 'Line':
                data['features'].append({
                    'type': 'Feature',
                    'id': index,
                    'properties': {
                        'balloonContent': 'Содержимое балуна',
                        'clusterCaption': 'Еще одна метка',
                        'hintContent': 'Текст подсказки'
                    },
                    'options': {
                        'strokeWidth': 2
                    },
                    'geometry':{
                        'type': 'LineString'                 
                    }
                })
                data['features'][index]['geometry']['coordinates'] = []
                for i in range(0,len(t)-1,2): data['features'][index]['geometry']['coordinates'].append([float(t[i]),float(t[i+1])])
        
        # Send message back to client
        # Write content as utf-8 data
        message = json.dumps(data,ensure_ascii=False,indent=1)
        self.wfile.write(bytes(message, "utf8"))
    except IOError:
        print("Error: File does not appear to exist.")     
    return

def run():
  print('starting server...')
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8080)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
run()