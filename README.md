
![alt text](https://picresize.com/images/rsz_1rsz_cyber-security-3400657_1280.jpg)

**SimpleCrypt_WS**

 SimpleCrypt_WS is a REST service that allows you to:  
  
* generate RSA key pairs  
* Encrypt data using RSA key pair  
* Decrypt data using RSA key pair  

Docker HUB: https://hub.docker.com/r/talziv/simplecrypt_ws

Run as container:

    docker run --rm -p 9999:80 talziv/simplecrypt_ws:latest

The project also has a swagger web interface at:  

    http://localhost:9999/api/spec.html 

 
  
And swagger spec.json at  

    http://localhost:9999/api/spec.json 

 
   
Postman demo collection:  

    https://www.postman.com/collections/e0129fa8057277b5bfd5  

  
SimpleCrypt-tools uses pycryptodome
