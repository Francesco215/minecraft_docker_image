This is the docker image we use for our minecraft server.  

To install the image run
```
docker build -t "image_name" .
```

Then run the image with
```
docker run -d -p 25565:25565 "image_name"
```

To attach to the image use
```
docker attach "image_name"
```

Once inside there should be a script called `start_server.sh` which will start the server.
