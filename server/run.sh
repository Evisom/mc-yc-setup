read -p "Enter port number: " port
read -p "Enter minRAM (in MB): " minRAM
read -p "Enter maxRAM (in MB): " maxRAM

docker run -e minRAM=$minRAM -e maxRAM=$maxRAM -p $port:25565 --name mc-yc-server-container -d --restart always -v $(pwd)/world:/server/world:rw mc-yc-server-image
