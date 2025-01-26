import websocket as ws_client

class ComfyWsUtil:
    def __init__(self, base_url):
        self.base_url = base_url
        self.ws:ws_client.WebSocket = None
    def ws(self,client_id:str):
        self.ws = ws_client.WebSocket()
        self.ws.connect(f"ws://{self.base_url}/ws?clientId={client_id}")

    def close(self):
        self.ws.close()
        self.ws = None

    def get_response(self):
        if self.ws is None: return None
        return self.ws.recv() 
