from http.server import BaseHTTPRequestHandler 
import json 
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from pegasus_final_complete import PegasusIndustrial 
 
class handler(BaseHTTPRequestHandler): 
    def do_GET(self): 
        from urllib.parse import urlparse, parse_qs 
        parsed = urlparse(self.path) 
        params = parse_qs(parsed.query) 
        ticker = params.get('ticker', ['GC=F'])[0] 
        market = params.get('market', ['gold'])[0] 
        system = PegasusIndustrial() 
        result = system.run(ticker, market) 
        self.send_response(200) 
        self.send_header('Content-type', 'application/json') 
        self.end_headers() 
        self.wfile.write(json.dumps(result).encode('utf-8')) 
