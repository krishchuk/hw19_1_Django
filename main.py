from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def get_html_content(self, html_file) -> str:
        with open(html_file, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        page_content = self.get_html_content('index.html')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
