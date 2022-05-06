This repo is aimed at bootstrapping a homelab or other installation in which one is hosting infrastructure built with Terraform, without using a public cloud or a filesystem as a backend.

It will launch a Postgres instance which you can use for Terraform backends

It will also launch a dnsmasq instance which initially serves a record for the host machine on which you run this, allowing access to Postgres by host.

To run this you will need a machine to run it on, which has networking enabled and docker installed. 

Typically, once you have filled in the config.yml file with your desired values, all you need do is run

    ./init.sh


Configuration for dnsmasq, and a docker-compose file will be generated, then docker-compose will bring up the services. To immediately put this into the background so you can log out, add -d to the end

    ./init.sh -d

Configure your dhcp servers or routers or whatever to dole out the host ip as a dns server, and you will be able to aim all your terraform at the given hostname.