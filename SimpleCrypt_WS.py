from flask import Flask, request, flash, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_restful import reqparse, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
import pdb
import json
import base64
import time         
from simplecrypttools import CryptTools

app = Flask(__name__)
#api = Api(app)
api = swagger.docs(Api(app), apiVersion='0.1')

@swagger.model
class EncryptDataRequest:
  resource_fields = {
      'publickey': fields.String,
      'content': fields.String
  }
  required = ['publickey', 'content']

@swagger.model
class EncryptDataResponse:
  resource_fields = {
      'encryptedContent': fields.Integer,
      'timestamp': fields.DateTime
  }
  required = ['encryptedContent', 'timestamp']

@swagger.model
class DecryptDataRequest:
      resource_fields = {
          'passphrase': fields.String,
          'privatekey': fields.String,
          'content': fields.String
      }
      required = ['content', 'privatekey', 'passphrase']
@swagger.model
class GenerateKeysModelRequest:
  resource_fields = {
      'passphrase': fields.String,
      'keysize': fields.Integer
  }
  required = ['passphrase']

  swagger_metadata = {
      'keysize': {
          'enum': [1024, 2048, 4096]
      }
  }

@swagger.model
class DecryptDataRequest:
  resource_fields = {
      'passphrase': fields.String,
      'privatekey': fields.String,
      'content': fields.String
  }
  required = ['content', 'privatekey', 'passphrase']

@swagger.model
class DecryptDataResponse:
  resource_fields = {
      'decryptedContent': fields.Integer,
      'timestamp': fields.DateTime
  }
  required = ['decryptedContent', 'timestamp']

@swagger.model
class GenerateKeysModelRequest:
  resource_fields = {
      'passphrase': fields.String,
      'keysize': fields.Integer
  }
  required = ['passphrase']

  swagger_metadata = {
      'keysize': {
          'enum': [1024, 2048, 4096]
      }
  }

@swagger.model
class GenerateKeysModelResponse:
  resource_fields = {
      'keysize': fields.Integer,
      'priavtekey': fields.String,
      'publickey': fields.String,
      'timestamp': fields.DateTime
  }
  required = ['keysize', 'priavtekey', 'publickey', 'timestamp']

class Decrypt_Data(Resource):
    @swagger.operation(
        notes='Decrypt data',
        responseClass=DecryptDataResponse.__name__,
        nickname='decrypt',
        parameters=[
            {
                "name": "DecryptData",
                "description": "Decrypt RSA encrypted BASE64 encoded data.",
                "required": True,
                "allowMultiple": False,
                "dataType": DecryptDataRequest.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Content decrypted successfuly."
            },
            {
                "code": 500 ,
                "message": "Invalid input"
            },
            {
                "code": 400,
                "message": "JSON request error"
            }
        ])
    def post(self):
        cryptapi = CryptTools()
        data = request.json
        #pdb.set_trace()
        response = {}
        response['decryptedContent'] = str(cryptapi.decrypte_with_rsa_key_b64(data['privatekey'], data['passphrase'], data['content']), 'ascii')
        response['timestamp'] = time.strftime("%d-%m-%Y %H:%M:%S")
        return response

class Encrypt_Data(Resource):
    @swagger.operation(
        notes='Encrypt data',
        responseClass=EncryptDataResponse.__name__,
        nickname='decrypt',
        parameters=[
            {
                "name": "EncryptData",
                "description": "Encrypt BASE64 encoded data with RSA key.",
                "required": True,
                "allowMultiple": False,
                "dataType": EncryptDataRequest.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Content Encrypted successfuly."
            },
            {
                "code": 500,
                "message": "Invalid input"
            },
            {
                "code": 400,
                "message": "JSON request error"
            }
        ])
    def post(self):
        cryptapi = CryptTools()
        data = request.json
        response = {}
        response['encryptedContent'] = str(cryptapi.encrypt_with_rsa_key_b64(data['publickey'], data['content']), 'ascii')
        response['timestamp'] = time.strftime("%d-%m-%Y %H:%M:%S")
        #print(response['encryptedContent'])
        return response

class Generate_Keys(Resource):
    @swagger.operation(
        notes='Creates a new keypair',
        responseClass=GenerateKeysModelResponse.__name__,
        nickname='create',
        parameters=[
            {
                "name": "GenerateKey",
                "description": "Generate a RSA key pair",
                "required": True,
                "allowMultiple": False,
                "dataType": GenerateKeysModelRequest.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Keys successfuly generated."
            },
            {
                "code": 500 ,
                "message": "Invalid input"
            },
            {
                "code": 400,
                "message": "JSON request error"
            }
        ])
    def post(self):
        data = request.json
        cryptapi = CryptTools()
        if ('keysize' in data):
            KeyPairResponse = cryptapi.generatekeypair(data['passphrase'], data['keysize'])
        else:
            KeyPairResponse = cryptapi.generatekeypair(data['passphrase'])
        response = {}
        response['keysize'] = KeyPairResponse['keysize']
        response['privatekey'] = str(base64.b64encode(KeyPairResponse['private']), 'ascii')
        response['publickey'] = str(base64.b64encode(KeyPairResponse['public']), 'ascii')
        response['timestamp'] = time.strftime("%d-%m-%Y %H:%M:%S")
        return response

class Index(Resource):
    @swagger.operation(
        notes='Info',
        nickname='info',
        responseMessages=[
            {
                "code": 200,
                "message": "Info JSON successfuly generated."
            }
        ])

    def get(self):
        data = {}
        data['Title'] = 'SimpleCrypt Micro Service'
        data['Version'] = '0.1'
        data['Maintainer'] = 'Tal Ziv'
        data['Github'] = 'https://github.com/TalZiv/'
        data['Description'] = 'Provides RSA content encryption and decryption RESTful micro service'
        return data

api.add_resource(Index, '/')
api.add_resource(Encrypt_Data, '/Encrypt_Data')
api.add_resource(Decrypt_Data, '/Decrypt_Data')
api.add_resource(Generate_Keys, '/Generate_Keys')

if __name__ == '__main__':
     app.run(port=5556, debug=False)
