.PHONY: all

SRC := ./src
CMD := poetry run
TESTS := ./tests

all: lint test

lint:
	$(CMD) isort --check --diff $(SRC)
	$(CMD) black --check --diff $(SRC)

format:
	$(CMD) isort $(SRC)
	$(CMD) black $(SRC)

test:
	$(CMD) pytest $(TESTS)
