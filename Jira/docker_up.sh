docker run -d -p 8080:8080 --name jira cptactionhank/atlassian-jira:latest

docker-ip() {
	docker inspect --format '{{ .NetworkSettings.IPAddress }}' "$@"
}

export JIRA_IP=`docker-ip jira`

docker run -d -p 8888:8888 --name notebook -e JIRA_IP=$JIRA_IP -v ~:/home/jovyan/work jupyter/scipy-notebook start-notebook.sh --NotebookApp.token=''
