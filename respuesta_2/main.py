from flask import Flask

from repository import Repository
from controller import Routes
from connector import ConnectorDatabase

if __name__ == '__main__':
    app = Flask(__name__)

    repository = Repository(ConnectorDatabase('localhost', 'root', 'root', 'gri', 3307))

    routes = Routes(app, repository)

    app.run(host='0.0.0.0', port=8080)




