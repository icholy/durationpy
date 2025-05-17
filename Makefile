build: clean
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf build dist *.egg-info

publish: build
	twine upload dist/*
