from channels.generic.websocket import AsyncWebsocketConsumer


class DashConsumer(AsyncWebsocketConsumer):

    


    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.connect()


    async def disconnect(self, close_code):

        await self.disconnect()
        

    async def receive(self, text_data):

        print(>>>>, text data)

        pass

