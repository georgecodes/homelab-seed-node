#!/usr/bin/env python3

import jinja2

data = {
    "local_data_mount": "./data",
    "dbhost": "stewie.ghmlabs.com",
    "name_server_pri": "192.168.0.1",
    "name_server_sec": "8.8.8.8"
}

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "docker-compose.yml.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(data)  # this is where to put args to the template renderer

print(outputText)

