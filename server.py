from datetime import datetime
import http.server
import socketserver
import json

def writefile(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(f"Location: {data['location']}\n")
            f.write(f"Units: {data['units']}\n")
            f.write(f"Date: {data['date']}\n")
        return True
    except Exception as e:
        print(f"Error writing file {filename}: {str(e)}")
        return False

def clean_message(message):
    if message['location'] is None:
        return None
    if message['units'] < 0:
        return None
    
    cleaned_message = {
        'location': message['location'].upper(),  # Assuming caps() function capitalizes the location
        'units': message['units'],
        'date': message['date']  # Assuming date is already in the correct format
    }
    
    return cleaned_message

# Handler for data POST requests
class DataPostHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            message = json.loads(post_data.decode('utf-8'))
            cleaned = clean_message(message)
            if cleaned:
                filename = "tmp/" + datetime.utcnow().strftime("%Y%m%d%H%M%S") + ".txt"
                if writefile(filename, cleaned):
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"Message saved successfully")
                else:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(b"Error saving message")
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid message format")
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON data")

# Set up a listener on port 8080
PORT = 8080
with socketserver.TCPServer(("", PORT), DataPostHandler) as httpd:
    print(f"Server listening on port {PORT}")
    httpd.serve_forever()
