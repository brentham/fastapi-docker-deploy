start:
	uvicorn main:app --reload

freeze:
	pip3 freeze > requirements.txt

depends:
	pip3 install -r requirements.txt