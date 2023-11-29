# Shared Vehicle Manager with IOT

## Ideal Structure
![IdealStructure](https://github.com/Eclipse-SDV-Hackathon-Accenture/Millennium_FleetManagement/assets/120576021/7954c92a-19f3-4e09-b9c8-ba28ca1bd5c7)


## For Hackathon
![ForHackathon](https://github.com/eclipse-sdv-blueprints/fleet-management/assets/120576021/a61234f9-720e-4e07-b4cf-958145295ce9)



- Change MonitorIP in forwarder-setting.env
- Send influxdb.token to /etc/forwarder/influxdb.token

# on the (local) host that you have started the back end components on
docker exec -it influxDB cat /tmp/out/fms-demo.token > /tmp/influxdb.token

# The FMS Forwarder needs to read the token required for authenticating to influxdb.
scp -P 2222 /tmp/influxdb.token root@127.0.0.1:/data/usr/fms/forwarder
