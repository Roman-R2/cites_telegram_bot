include .env
export

# ----- Docker section ---------------------------------------
# ----- Docker prod section -----
docker-prod-down:
	docker-compose -f docker-compose.yml down -v --remove-orphans

docker-prod-build-up:
	docker-compose -f docker-compose.yml up -d --build

docker-prod-logs:
	docker-compose -f docker-compose.yml logs -f

docker-commit:
	docker commit grasian-cite-python-cli ${REGISTRY_ADDRESS}/grasian-cite-python-cli:${IMAGE_TAG}

docker-push:
	docker push ${REGISTRY_ADDRESS}/grasian-cite-python-cli:${IMAGE_TAG}

docker-pull:
	docker pull ${REGISTRY_ADDRESS}/grasian-cite-python-cli:${IMAGE_TAG}

docker-images-to-hub: docker-commit docker-push

# ----- Code section -----
check-code:
	isort app/
	flake8 --extend-ignore E501 app/

# ----- VPS loading section -----
some-scp:
	scp docker-compose-production-load.yml root@${REMOTE_VPS_IP}:/root/grasian-cite
	scp Makefile root@${REMOTE_VPS_IP}:/root/grasian-cite
	scp .env root@${REMOTE_VPS_IP}:/root/grasian-cite

vds-server-up: docker-pull
	docker-compose -f docker-compose-production-load.yml down -v --remove-orphans
	docker-compose -f docker-compose-production-load.yml up -d
