# Setting up the Raspberry Pi

## Installation

* Set up your Raspberry Pi with a Linux operating system (e.g. Raspbian) and login (either directly or via ssh). Explaining how to do that is out of scope. However, there are plenty of resources online.

* The following lines have to be executed to install docker. The last line confirms that the installation was successful.
```bash
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker pi
sudo reboot
docker run hello-world
```

* Then install docker-compose. The last line prints out the docker-compose version which confirms a successful installation.
```bash
sudo apt-get install -y python3-pip python3-dev
sudo pip3 install docker-compose
docker-compose --version
```

* You should now clone this repo ```git clone https://github.com/gbusch/bme680_home_monitor.git``` and change to the raspberrypi folder: ```cd bme680_home_monitor/raspberrypi```.

* Now you need to run the build command: ```docker-compose build```. You need to run this command only once and after changes in the mqtt-forwarder.

* Start the docker containers with ```docker-compose up -d```. 

* If you want to stop the containers later, you can do that with ```docker-compose down```.


## Setting up a telegram alert
TBD


## Docker containers
The following docker containers will be started:
 
### MQTT-broker (Eclipse Mosquitto)
Eclipse Mosquitto is a light-weight MQTT broker. 
You can use the MQTT broker for other projects as well. Just choose a different topic to publish on.
It will be available in the home network under the address of your Raspberry Pi (since it is in the local network the IP address should start with 192.168.178.*) and port 1883. This is the default port for unencrypted MQTT.

### Database (InfluxDB)
InfluxDB is a database specially suited for timeseries data. The data is stored in the directory ```/var/lib/influxdb```. This folder is mounted to the directory ```./influxdb/data``` on the host machine. This allows to keep data also when the docker-container is shutdown.

### Dashboard (Grafana)
TBD

### MQTT forwarder script
TBD
