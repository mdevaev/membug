all:
	true

pylint:
	pylint --rcfile=pylint.ini \
		*.py \
		--output-format=colorized 2>&1 | less -SR

pypi:
	python setup.py register
	python setup.py sdist upload

clean:
	rm -rf build dist *.egg-info
	find . -type f -name '*.pyc' -delete
	find . -type d -name __pycache__ -delete
