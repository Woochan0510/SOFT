from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparse
import io

class ChatServer(BaseHTTPRequestHandler):
    messages = []

    def __get_Parameter(self, key):
        if not hasattr(self, "_ChatServer__param"):
            if "?" in self.path:
                self.__param = dict(urlparse.parse_qsl(self.path.split("?")[1], True))
            else:
                self.__param = {}
        if key in self.__param:
            return self.__param[key]
        return None

    def __set_Header(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def __set_Body(self, data):
        self.wfile.write(data.encode())

    def do_GET(self):
        # Display the chat form and messages
        chat_messages = "<br>".join(self.messages)
        body = f"""
        <!DOCTYPE html>
        <html>
            <head><title>Chat Server</title></head>
            <body>
                <h2>Chat Room</h2>
                <div>{chat_messages}</div>
                <form method='post'>
                    <input type='text' name='message'>
                    <input type='submit' value='Send'>
                </form>
            </body>
        </html>"""
        
        self.__set_Header(200)
        self.__set_Body(body)

    def do_POST(self):
        # Handle incoming chat messages
        self.__set_Header(200)
        message = self.__get_Parameter('message')
        if message:
            self.messages.append(message)
        self.do_GET()  # Redirect to GET to show updated messages

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8080), ChatServer)
    print('Chat server is running...')
    httpd.serve_forever()