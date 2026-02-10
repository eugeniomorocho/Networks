from http.server import HTTPServer, BaseHTTPRequestHandler  # Minimal HTTP server
from socketserver import ThreadingMixIn                    # Allows threaded server
import urllib.parse                                       # Parse form data

# The image file and correct answer
IMAGE_FILE = "cat_1.jpg"
CORRECT_ANSWER = "cat"

# Minimal request handler
class Handler(BaseHTTPRequestHandler):
    # Handle GET requests: show form or image
    def do_GET(self):
        if self.path == f"/{IMAGE_FILE}":  # Serve the image
            try:
                with open(IMAGE_FILE, "rb") as f:  # Open image in binary mode
                    self.send_response(200)
                    self.send_header("Content-type", "image/jpeg")
                    self.end_headers()
                    self.wfile.write(f.read())      # Send image bytes
            except FileNotFoundError:
                self.send_error(404, "Image not found")
        else:  # Serve HTML form
            html = f"""
            <html><body>
            <h2>Guess the Image Game</h2>
            <img src="{IMAGE_FILE}" width="300"><br><br>
            <form method="POST">
              Name: <input name="name"><br>
              Guess: <input name="guess"><br>
              <input type="submit">
            </form>
            </body></html>
            """
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())  # Send HTML to browser

    # Handle POST requests: process form submission
    def do_POST(self):
        length = int(self.headers['Content-Length'])           # Length of POST data
        post = self.rfile.read(length).decode()               # Read POST data
        data = urllib.parse.parse_qs(post)                    # Parse form fields
        name = data.get("name", ["Unknown"])[0]               # Get name field
        guess = data.get("guess", [""])[0].lower()            # Get guess field, lowercase

        # Check guess
        if guess == CORRECT_ANSWER.lower():
            msg = f"Congrats {name}, you won!"
        else:
            msg = f"Sorry {name}, wrong guess."

        # Respond with result page
        html = f"<html><body><h2>{msg}</h2><a href='/'>Try Again</a></body></html>"
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

# Threaded HTTP server
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in separate threads."""
    pass

# Run server
if __name__ == "__main__":
    server_address = ("", 8080)              # Listen on all interfaces, port 8080
    httpd = ThreadedHTTPServer(server_address, Handler)  # Threaded server
    print("Server running on http://localhost:8080")
    httpd.serve_forever()                    # Start server, runs forever
