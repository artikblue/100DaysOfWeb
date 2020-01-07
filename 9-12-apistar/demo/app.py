import json
from typing import List

from apistar import App, Route, types, validators
from apistar.http import JSONResponse


# helpers

def _load_connections_data():
    with open('connection_data.json') as f:
        connections = json.loads(f.read())
        return {connection["id"]: connection for connection in connections}



connections = _load_connections_data()

VALID_COUNTRIES = set([connection["country"]
                          for connection in connections.values()])

CON_NOT_FOUND = 'Connection not found'

# definition

class Connection(types.Type):
    id = validators.Integer(allow_null=True)
    user_agent = validators.String(max_length=300)
    country = validators.String(enum=list(VALID_COUNTRIES))
    date = validators.String()
    ipv4_addr = validators.String(max_length=15)

# API methods

def list_connections() -> List[Connection]:
    return [Connection(connection[1]) for connection in sorted(connections.items())]

def get_connection(connection_id: int) -> JSONResponse:
    connection = connections.get(connection_id)

    if not connection:
        error = {'error': CON_NOT_FOUND}
        return JSONResponse(error, status_code = 404)
    
    return JSONResponse(Connection(connection), status_code=200)

def create_connection(connection: Connection) -> JSONResponse:
    connection_id = len(connections.keys()) + 1
    connection.id = connection_id
    connections[connection_id] = connection

    return JSONResponse(Connection(connection), status_code = 201)

def update_connection(connection_id: int, connection: Connection) -> JSONResponse:
    if not connections.get(connection_id):
        error = {'error': CON_NOT_FOUND}
        return JSONResponse(error, status_code = 404)
    
    connection.id = connection_id
    connections[connection_id] = connection
    return JSONResponse(Connection(connection), status_code=200)

def delete_connection(connection_id: int) -> JSONResponse:
    if not connections.get(connection_id):
        error = {'error': CON_NOT_FOUND}
        return JSONResponse(error, status_code = 404)
    
    del connections[connection_id]

    return JSONResponse({}, status_code = 204)

routes = [
    Route('/', method='GET', handler=list_connections),
    Route('/{connection_id}/', method='GET', handler=get_connection),
    Route('/', method='POST', handler=create_connection),
    Route('/{connection_id}/', method='PUT', handler=update_connection),
    Route('/{connection_id}/', method='DELETE', handler=delete_connection)
]

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)