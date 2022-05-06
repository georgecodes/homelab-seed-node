#!/usr/bin/env python3

import jinja2
import yaml

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

def read_config():
    with open(r'config.yml') as file:
        return yaml.load(file, Loader=yaml.FullLoader)

def write_dnsmasq_conf(conf):
    template = templateEnv.get_template("dnsmasq.conf.j2")
    write_template(conf, template, "config/dnsmasq.conf")

def write_host_file(conf):
    template = templateEnv.get_template("hosts.j2")
    write_template(conf, template, "config/hosts")

def write_docker_compose(conf):
    template = templateEnv.get_template("docker-compose.yml.j2")
    write_template(conf, template, "docker-compose.yml")

def write_template(conf, template, dest):
    f = open(dest, "w")
    f.write(template.render(conf))
    f.close()

conf = read_config()
write_dnsmasq_conf(conf)
write_host_file(conf)
write_docker_compose(conf)