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


## Docker containers
The following docker containers will be started:
 
### MQTT-broker (Eclipse Mosquitto)
Eclipse Mosquitto is a light-weight MQTT broker. 
You can use the MQTT broker for other projects as well. Just choose a different topic to publish on.
It will be available in the home network under the address of your Raspberry Pi (since it is in the local network the IP address should start with 192.168.178.*) and port 1883. This is the default port for unencrypted MQTT.

### Database (InfluxDB)
InfluxDB is a database specially suited for timeseries data. The data is stored in the directory ```/var/lib/influxdb```. This folder is mounted to the directory ```./influxdb/data``` on the host machine. This allows to keep data also when the docker-container is shutdown.

### Dashboard (Grafana)
Grafana is an open-source dashboard and monitoring tool. It is accessible from the browser under ```<address of your Raspberry Pi>:3000```. A powerful feature in the newest versions is provisioning. This allows to save the dashboards as well as configuration for data sources and notifications in json and yaml files and provide them to Grafana when the container is started. This way, dashboards can be easily shared and version-controlled together with the project.

The example dashboard will automatically be loaded when the docker containers are started and is accessible in the browser under ```<address of your Raspberry Pi>:3000/d/kpBr4Nzgz/home-measurements?orgId=1```.

#### Changing the dashboard
* Sign in to Grafana using the credentials provided in the [docker-compose.yml](docker-compose.yml) (at the moment admin/secret-password).
* Adjust the dashboard
* Click save. You cannot save a provisioned dashboard from the Grafana UI, instead choose "copy JSON to clipboard". Copy this into the file [./grafana/dashboards/home_measurements.json](./grafana/dashboards/home_measurements.json) and save.
* Next time you restart the container, the new version will be provisioned.

#### Setting up a telegram alert
Grafana also offers alerting and supports many different notification channels. As an example, I configured an alert that is raised whenever the indoor air quality exceeds a value of 200. 

With the following steps, you can configure notifications to Telegram when this alert is raised:

* Create a new bot as described in the [Telegram Documentation](https://core.telegram.org/bots#6-botfather). Note down the bot token.
* Create a telegram group with people that should be alerted and invite the bot to this group.
* Use curl or place this in a browser: ```https://api.telegram.org/bot<TOKEN>/getUpdates```.
* The response returns a json object in which you find the key "chat". Note down the number after "id" (including the dash).
* You can find an example configuration in [./grafana/provisioning/notifiers/telegram.yml.example](./grafana/provisioning/notifiers/telegram.yml.example). Remove the file-ending ".example" and insert bot token and chat id.
* Restart Grafana.


### MQTT forwarder script
This simple python script subscribes to the same topic that the ESP32 publishes to and writes all messages that it receives into the InfluxDB database. The script runs in a Docker container as well so that you do not need to worry about python configuration or the like.

Please note that the first time you use it and whenever you make changes to the script you need to rebuild the container with ```docker-compose build```.
