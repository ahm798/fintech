build:
	docker compose  -f local.yml up  --build -d --remove-orphans
up:
	docker compose  -f local.yml up  -d
down:
	docker compose  -f local.yml down
down-volumes:
	docker compose  -f local.yml down --volumes

b-config:
	docker compose -f local.yml config

makemigrations:
	docker compose -f local.yml --rm exec api python3 manage.py makemigrations

migrate:
	docker compose -f local.yml --rm  exec api python3 manage.py migrate

collectstatic:
	docker compose -f local.yml --rm  exec api python3 manage.py collectstatic --noinput
createsuperuser:
	docker compose -f local.yml --rm  exec api python3 manage.py createsuperuser
shell:
	docker compose -f local.yml --rm  exec api python3 manage.py shell

flush:
	docker compose -f local.yml --rm  exec api python3 manage.py flush

network:
	docker network inspect local_network

psql:
	docker compose -f local.yml --rm  exec psql psql -h db -U postgres -d postgres


