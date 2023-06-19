# pip3 install Flask flask_jwt_extened jwt websockets


import asyncio
import websockets

from jwt import decode as jwt_decode
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'SPJhvL2RtS8ytrT27gaa54rX0uomDpuavxlRUEgpfXaSwarGXAV1yvgY'  
jwt = JWTManager(app)


# WebSocket Endpoint
@app.route('/ws')
def websocket_handler(websocket, path):
    try:
        async for message in websocket:
            await handle_message(websocket, message)
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected")

# Template for message handling
async def handle_message(websocket, message):

    response = f"Received message: {message}"
    await websocket.send(response)

# may need to change endpoint
@app.route('/api/token', methods=['POST'])
def request_token():
    
    # mnemonic or private key instead
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Generic authentication. 
    # most likely based off private key or mnemonic
    if username == 'your_username' and password == 'your_password':
        access_token = create_access_token(identity=username)
        return jsonify({'token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Basic JWT verification
@app.route('/protected', methods=['GET'])
def protected_route():
    
    token = request.headers.get('x-device-token')
    if not token:
        return 'Missing token', 401

    try:

        # access to JWT token payload if need be
        token_payload= jwt_decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        
        # o/w return
        return 'Access granted', 200
    
    except jwt.InvalidTokenError:
        return 'Invalid token', 401


@app.route('/api/device', methods=['POST'])
@jwt_required()
def create_device():

    pass


@app.route('/api/vpn/servers/<int:id>', methods=['POST'])
@jwt_required()
def create_vpn_server(id):

    pass


@app.route('/api/blockchain/sentinel/<walletAddress>/nodes/<nodeAddress>/sessions/<sessionId>', methods=['POST'])
@jwt_required()
def create_blockchain_session(walletAddress, nodeAddress, sessionId):

    pass


@app.route('/api/state', methods=['GET'])
@jwt_required()
def get_state():

    pass


@app.route('/api/state', methods=['PUT'])
@jwt_required()
def update_state():

    pass


@app.route('/api/countries', methods=['GET'])
@jwt_required()
def get_countries():

    pass


@app.route('/api/vpn/countries', methods=['GET'])
@jwt_required()
def get_vpn_countries():

    pass


@app.route('/api/servers', methods=['GET'])
@jwt_required()
def get_servers():

    pass


@app.route('/api/vpn/servers', methods=['GET'])
@jwt_required()
def get_vpn_servers():

    pass


@app.route('/api/servers/<int:id>/rating', methods=['POST'])
@jwt_required()
def rate_server(id):

    pass


@app.route('/api/vpn/servers/<int:id>/rating', methods=['POST'])
@jwt_required()
def rate_vpn_server(id):

    pass


@app.route('/api/profile', methods=['GET'])
@jwt_required()
def get_profile():

    pass


@app.route('/api/subscription', methods=['GET'])
@jwt_required()
def get_subscription():

    pass


@app.route('/api/device/user', methods=['GET'])
@jwt_required()
def get_user_devices():

    pass


@app.route('/api/profile', methods=['POST'])
@jwt_required()
def create_profile():

    pass


@app.route('/api/device', methods=['PUT'])
@jwt_required()
def update_device():

    pass


@app.route('/api/profile', methods=['DELETE'])
@jwt_required()
def delete_profile():

    pass


@app.route('/api/device', methods=['DELETE'])
@jwt_required()
def delete_device():

    pass


@app.route('/api/wallet', methods=['GET'])
@jwt_required()
def get_wallet():

    pass


@app.route('/api/blockchain/sentinel/<walletAddress>/balance', methods=['GET'])
@jwt_required()
def get_sentinel_balance(walletAddress):

    pass


@app.route('/api/wallet', methods=['PUT'])
@jwt_required()
def update_wallet():

    pass


@app.route('/api/wallet/mnemonic', methods=['GET'])
@jwt_required()
def get_wallet_mnemonic():

    pass


@app.route('/api/wallet/servers', methods=['GET'])
@jwt_required()
def get_wallet_servers():

    pass


@app.route('/api/blockchain/sentinel/<walletAddress>/nodes/<nodeAddress>/subscriptions', methods=['GET'])
@jwt_required()
def get_node_subscriptions(walletAddress, nodeAddress):

    pass


@app.route('/api/dns', methods=['GET', 'PUT'])
@jwt_required()
def dns_handler():
    if request.method == 'GET':

        pass
    elif request.method == 'PUT':

        pass


if __name__ == '__main__':
    app.run()
    ws_server = websockets.server.serve(websocket_handler, 'localhost', 8000)
    asyncio.get_event_loop().run_until_complete(ws_server)
    asyncio.get_event_loop().run_forever()
