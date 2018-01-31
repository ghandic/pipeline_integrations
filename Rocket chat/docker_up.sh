docker run --name db -d mongo:3.2 mongod --smallfiles
docker run --name rocketchat -p 3000:3000 --env ROOT_URL=http://localhost --link db:db -d rocket.chat

docker-ip() {
	docker inspect --format '{{ .NetworkSettings.IPAddress }}' "$@"
}

export ROCKET_IP=`docker-ip rocketchat`

docker run -d -p 8888:8888 --name notebook -e ROCKET_IP=$ROCKET_IP -v ~:/home/jovyan/work jupyter/scipy-notebook start-notebook.sh --NotebookApp.token=''
