import http.server
import ssl
import os
import sys

def run_server(port=4443):
    # Check for certificate files
    if not (os.path.exists('cert.pem') and os.path.exists('key.pem')):
        print("Error: Certificate files not found. Run the following commands to generate them:")
        print("\nopenssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365")
        print("\nMake sure to add cert.pem as a trusted certificate in your browser.")
        sys.exit(1)

    # Set up a simple HTTP server
    handler = http.server.SimpleHTTPRequestHandler
    
    # Create an HTTPS server with the certificate
    httpd = http.server.HTTPServer(('localhost', port), handler)
    
    # Add SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print(f"Server started at https://localhost:{port}")
    print("Place your amazon-login.html file in the same directory as this script")
    print("To access the phishing page, open https://localhost:{port}/amazon-login.html")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    port = 4443  # Default port
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port '{sys.argv[1]}'. Using default port {port}.")
    
    run_server(port)
