from http.server import BaseHTTPRequestHandler 
import json 
import sys 
import os 
import traceback 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
 
try: 
    from pegasus_final_complete import PegasusIndustrial 
    MODULE_READY = True 
except ImportError as e: 
    MODULE_READY = False 
    IMPORT_ERROR = str(e) 
 
class handler(BaseHTTPRequestHandler): 
    def do_GET(self): 
        try: 
            if not MODULE_READY: 
                raise Exception(f"Ä£¿éµ¼ÈëÊ§°Ü: {IMPORT_ERROR}") 
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
            self.wfile.write(json.dumps(result, ensure_ascii=False).encode('utf-8')) 
        except Exception as e: 
            self.send_response(500) 
            self.send_header('Content-type', 'application/json') 
            self.end_headers() 
            self.wfile.write(json.dumps({"error": str(e), "traceback": traceback.format_exc()}).encode('utf-8')) 
