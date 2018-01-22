# Pipeline integrations

This repository hosts a series of shellscripts and notebooks demonstrating how to integrate communication services into a pipeline

At present the integrations included are:

* Slack
* Jira
* Rocket Chat
* Email (Hotmail)

This repo relies on the use of Docker, so ensure it is installed before continuing:

### Docker download links
* [Windows](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe)
* [Mac](https://download.docker.com/mac/stable/Docker.dmg)

[*More info on Docker*](https://www.docker.com/)

### Ngrok download links
* [Windows](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip)
* [Mac](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip)

Then run unzip the downloaded file: `unzip /path/to/ngrok.zip`

Ngrok can then be used as follows: `./ngrok http PORT` eg `./ngrok http 3000`

[*More info on Ngrok*](https://ngrok.com/)
