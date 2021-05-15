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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


""" def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message) """

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    
    qtd = ""

    while not qtd.isdecimal() or int(qtd) < 0:
        qtd = input("Deseja Cadastrar quantos funcionarios?")

    for i in range(int(qtd)):
        print("Por favor insira os danos para o cadastro do ",i+1,"° cliente")
        _nome = input("nome:")
        while True:
            _cpf = input("cpf:")
            if _cpf.isdigit():
                break
            else:
                print("CPF inválido")
        _endereco = input("endereco:")
        response = stub.Cadastra(helloworld_pb2.CadastrarCli_Request(nome=_nome,cpf=int(_cpf),endereco=_endereco))
        print("O ID do Cliente é:",response.id)
    
    _escolha = escolha()

    while True:
        if _escolha == "id":
            _id = ""
            while not _id.isdecimal():
                _id = input("Digite um ID por favor:")
                if not _id.isdecimal():
                    print("!!! ID não valido !!!")
            response = stub.ObtemPorID(helloworld_pb2.ObterCliID_Request(id=int(_id)))
        else:
            while not _cpf.isdecimal():
                _cpf = input("Digite um CPF por favor:")
                if not _cpf.isdecimal():
                    print("!!! CPF não valido !!!")
            response = stub.ObtemPorID(helloworld_pb2.ObterCliCPF_Request(cpf=_cpf))

        if response.id == 0:
                print("Não há Clientes com esse ID")
        else:
                print("Nome:",response.nome,"\nCPF:",response.cpf,"\nEndereco:",response.endereco,
                "\nID:",response.id)

        decisao = ""
        while decisao != "s" and decisao != "n":
            decisao = input("Deseja continuar?[S/N]").lower()
        if decisao == 'n':
            break


def escolha():
        escolha = ""
        while escolha != "id" and escolha != "cpf":
            escolha = input("Deseja Pesquisar Clientes por ID ou CPF?").lower()
        return escolha

if __name__ == '__main__':
    logging.basicConfig()
    run()
