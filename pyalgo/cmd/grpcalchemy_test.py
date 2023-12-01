from grpcalchemy.orm import Message, StringField
from grpcalchemy import Server, Context, grpcmethod

class HelloMessage(Message):
    text: str

class HelloService(Server):
    @grpcmethod
    def Hello(self, request: HelloMessage, context: Context) -> HelloMessage:
        return HelloMessage(text=f'Hello {request.text}')

if __name__ == '__main__':
    HelloService.run()