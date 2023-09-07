import http.server
import socketserver

# the extra part of the url (.../specification/...)
specification_repo_path = "specification"

# the directory we want to serve files from
directory = "docs"

# Define a custom request handler that includes the custom part in the URL
class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        print(path)
        path_components = path.split('/')
        path = super().translate_path(path)
        # Add the custom part to the URL
        return f"{directory}/{'/'.join(path_components[2:])}"

# Create a socket server with the custom request handler
with socketserver.TCPServer(("localhost", 8080), CustomRequestHandler) as httpd:
    print(f"Serving at http://localhost:8080/{specification_repo_path}/")
    httpd.serve_forever()
