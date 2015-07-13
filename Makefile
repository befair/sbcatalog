help:
	@echo '**SBCatalog Help**'
	@echo 'make            Print this help'
	@echo
	@echo 'Whole app commands:'
	@echo 'make up         Download and start all'
	@echo 'make ps         Container status'
	@echo 'make logs       See all logs'
	@echo 'make stop       Stop all containers'
	@echo 'make restart    Restart all containers'
	@echo 'make rm         Delete containers'
	@echo 'make test       Run all tests'
	@echo
	@echo 'Container commands:'
	@echo 'make logs-back  See only backend logs'
	@echo 'make back       Debug in backend via iPython'

up:
	@docker-compose up -d
	@docker-compose ps

logs log:
	@docker-compose logs

logs-back log-back:
	@docker-compose logs back

start:
	@docker-compose start
	@docker-compose ps

stop:
	@docker-compose stop
	@docker-compose ps

restart:
	@docker-compose restart
	@docker-compose ps

ps:
	@docker-compose ps

t:
	@docker-compose run --rm test /bin/bash

front fe frontend ui:
	@docker-compose run --rm front /bin/bash

back be backend api:
	@docker-compose run --rm back /bin/bash

shell:
	@docker-compose run --rm back ipython

update-geodb:
	@docker-compose run --rm back /code/api/run.py update-geodb

rmall: rm rmc rmi
	@echo 'All containers/images removed!'

rm:
	@docker-compose stop
	@docker-compose rm -f
	@docker rmi -f befair/sbcatalog-{test,front,back}

rmc:
	@docker rm -f $(docker ps -aq)

rmi:
	@docker rmi -f $(docker images -aq)

test: test-unit test-integration
	@echo 'All tests passed!'

test-unit:
	@echo 'TODO: unit test'

test-integration:
	@docker-compose run test py.test /code/test/integration
