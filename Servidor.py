# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:32:31 2023

@author: Juan Bernal Martinez
"""

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import math

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('192.168.1.107', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(pow)

    def suma(x, y):
        return x + y
    server.register_function(suma, 'suma')
    
    def resta(x,y):
        return x-y
    server.register_function(resta, 'resta')

    def division(x,y):
        return x/y
    server.register_function(division, 'division')
    
    def raiz(x):
        return math.sqrt(x)
    server.register_function(raiz, 'raiz')
    
    class MyFuncs:
        def multiplicacion(self, x, y):
            return x * y

    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()