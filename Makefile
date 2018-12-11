VERSION=$(shell grep version= setup.py | sed "s/^[ ]*version='//g;s/',$$//g")
TWINE_ARGS=-u $(shell pass dev/pypi.python.org/user) -p $(shell pass dev/pypi.python.org/pass)
PYTHON=$(shell which python3)

$(info VERSION:$(VERSION))
$(info PYTHON:$(PYTHON) $(shell $(PYTHON) --version))
#$(info TWINE_ARGS:$(TWINE_ARGS))

.PHONY:
all : build

.PHONY : clean
clean:
	$(PYTHON) setup.py clean
	rm -rf dist/*
	rm -rf build/*
	rm -rf stdplus.egg-info

.PHONY : deploy
deploy: clean install publish
	twine upload $(TWINE_ARGS) dist/*

.PHONY: publish
publish:
	$(MAKE) -C docs publish

.PHONY : sdist
sdist:
	$(PYTHON) setup.py sdist bdist_wheel

.PHONY : test
test :
	$(PYTHON) setup.py develop
	$(PYTHON) setup.py nosetests -s

.PHONY : build
build: test sdist
	$(PYTHON) setup.py build


.PHONY : install
install: build
	$(PYTHON) setup.py install

