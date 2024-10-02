build: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf build dist *.egg-info

publish: build
	twine upload dist/*
