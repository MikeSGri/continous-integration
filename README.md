# continous-integration

## primero corra asegurate de estar en directorio correcto, que se pueda visualizar Dockerfile 
docker build -t ci .

## una ves creada la imagen corra lo siguiente 
docker run -it -d --rm -p 8001:8000 ci 

## valide la connecion
en tu local corra  http://127.0.0.1:8001/users