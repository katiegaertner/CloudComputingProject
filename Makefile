install:
	pip3 install --upgrade pip &&\
	pip3 install -r requirements.txt
	pip3 install --upgrade google-cloud-BigQuery
	python3 -m pip install flask

test:
	python -m pytest -vv test_hello.py

format:
	python3 -m black hello.py

lint:
	pylint --disable=R,C hello.py

all: install lint test