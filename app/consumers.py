from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
class MyCon(SyncConsumer):

    def websocket_connect (self,event):
        print("someone connected",event)
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive (self,event):
        print("someone sent message")
        print(event)

    def websocket_disconnect (self,event):
        print("someone disconnected",event)
        raise StopConsumer()