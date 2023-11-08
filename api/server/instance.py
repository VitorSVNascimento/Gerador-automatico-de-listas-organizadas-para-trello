from flask import Flask
from api.server import constants as const
class Server:
    def __init__(self,):
        self.app = Flask(__name__)
    
    def run(self,):
        self.app.run(const.SERVER_HOST,const.SERVER_PORT,debug=True)

server = Server()