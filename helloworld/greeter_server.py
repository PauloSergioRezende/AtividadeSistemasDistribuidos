# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

Clientes = []

class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def Cadastra(self, request, context):
        Cliente = [request.nome, request.cpf, request.endereco,len(Clientes)+1]
        Clientes.append(Cliente)
        print("O cliente, "+Cliente[0]+" foi incluso.")
        return helloworld_pb2.CadastrarCli_Reply(id = Cliente[3])

    def ObtemPorCpf(self, request, context):
        if len(Clientes) != 0:
            for Cliente in Clientes:
                if request.cpf == Cliente[1]:
                    return helloworld_pb2.ObterCli_Reply(nome=Cliente[0],cpf=Cliente[1],endereco=Cliente[2],id=Cliente[3])
        return helloworld_pb2.ObterCli_Reply(nome="0",cpf=0,endereco="0",id=0)
    
    def ObtemPorID(self, request, context):
        if len(Clientes) != 0:
            for Cliente in Clientes:
                if request.id == Cliente[3]:
                    return helloworld_pb2.ObterCli_Reply(nome=Cliente[0],cpf=Cliente[1],endereco=Cliente[2],id=Cliente[3])
        return helloworld_pb2.ObterCli_Reply(nome="0",cpf=0,endereco="0",id=0)


    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
