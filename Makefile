start:
	uvicorn main:app --reload

freeze:
	pip3 freeze > requirements.txt

depends:
	pip3 install -r requirements.txt

build-dev:
	docker build -t fast-test-cvs:dev .

run-dev:
	docker run -it fast-test-cvs:dev sh

start-dev:
	docker run -p 85:80 fast-test-cvs:dev

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down