# irr-gui

[![License](https://img.shields.io/github/license/natesales/irr-gui?style=for-the-badge)](https://github.com/natesales/irr-gui/blob/master/LICENSE)
[![Release](https://img.shields.io/github/v/release/natesales/irr-gui?style=for-the-badge)](https://github.com/natesales/irr-gui/releases)
[![Docker](https://img.shields.io/badge/docker-natesales/irr--gui-blue?link=https://hub.docker.com/repository/docker/natesales/irr-gui&style=for-the-badge&logo=docker)](https://hub.docker.com/natesales/irr-gui)

Web UI for IRR object management.

![Screenshot](screenshot.png)

### Installation
irr-gui is available as a [Docker image](https://hub.docker.com/r/natesales/irr-gui) for easy installation. A simple [compose file](https://github.com/natesales/irr-gui/blob/master/docker-compose.yml) is also provided if you're looking to go that route.

### One line quickstart
```bash
docker run -p 80:80 -e IRRGUI_ASN=34553 -e 'IRRGUI_NETWORK_NAME=Nathan Sales' -e IRRGUI_IRR_SERVER=rr.ntt.net natesales/irr-gui:latest
```

### Environment variables
| Name                | Usage                        |
| ------------------- | ---------------------------- |
| IRRGUI_ASN          | Your ASN                     |
| IRRGUI_NETWORK_NAME | Your network name            |
| IRRGUI_IRR_SERVER   | IRR server to run queries on |
