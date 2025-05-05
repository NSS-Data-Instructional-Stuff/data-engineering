## Lab 11.1 

### Introduction

In this lab you will be connecting a server to a client with gRPC passing a simple message between the two. 

### Part 1
Make sure you have a virtual environment configured and a requirements.txt file in your root directory. Add grpcio and grpcio-tools to the requirements.txt file. Install them. 

### Part 2
Create a service.proto file and define your interface.  Here is an example: 

```
    syntax = "proto3";

    service MyService {
      rpc MyMethod (MyRequest) returns (MyResponse);
    }

    message MyRequest {
      string message = 1;
    }

    message MyResponse {
      string message = 1;
    }
```
### Part 3
Now you will want to use the .protoc command to generate some boiler plate code from the .proto file. Run the following in the root of your project:
```
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
```

This command should generate two files: service_pb2.py (containing the message classes) and service_pb2_grpc.py (containing the client and server classes)

### Part 4

Create a gRPC Server. This server will communicate to the client that you will create in the next part.  Here is a small example server: 

```
    import grpc
    from concurrent import futures
    import service_pb2
    import service_pb2_grpc

    class MyServiceServicer(service_pb2_grpc.MyServiceServicer):
        def MyMethod(self, request, context):
            return service_pb2.MyResponse(message=f"Hello, {request.message}!")

    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()

    if __name__ == '__main__':
        serve()
```

### Part 5
Create a Client. The client will pass a message back to the server and get a response. Here is an example client. 

```
    import grpc
    import service_pb2
    import service_pb2_grpc

    def run():
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = service_pb2_grpc.MyServiceStub(channel)
            response = stub.MyMethod(service_pb2.MyRequest(message='World'))
        print(f"Received: {response.message}")

    if __name__ == '__main__':
        run()
```

### Part 6
Start the server in one terminal. It will continue to run until you push ctrl C.  Run the client, and print the completed message to the rerminal. 

### Notes: 
This is class based. While we are doing functional programming mainly in this course, and the industry is moving that direction, there are some times where classes are needed as the structure of the library you are using depends on them. 