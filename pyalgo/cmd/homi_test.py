from homi import App, Server
from homi.extend.service import reflection_service, health_service


from helloworld_pb2 import DESCRIPTOR

svc_desc = DESCRIPTOR.services_by_name['Greeter']

app = App(
    services=[
        svc_desc,
        reflection_service,
        health_service,
    ]
)

# unary-unary method
@app.method('helloworld.Greeter')
def SayHello(name, **kwargs):
    print(f"{name} is request SayHello")
    return {"message": f"Hello {name}!"}


# or 
@app.method('helloworld.Greeter','SayHello')
def hello(request,context):
    print(f"{request.name} is request SayHello")
    return {"message": f"Hello {request.name}!"}

# or
def hello_func(request,context):
    return {"message":"hi"}

app.register_method('helloworld.Greeter','SayHello',hello_func)

if __name__ == '__main__':
    server = Server(app)
    server.run()