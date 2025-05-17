from setuptools import setup

setup(
    name         = 'durationpy',
    description  = 'Module for converting between datetime.timedelta and Go\'s Duration strings.',
    url          = 'https://github.com/icholy/durationpy',
    author       = 'Ilia Choly',
    author_email = 'ilia.choly@gmail.com',
    download_url = 'https://github.com/icholy/durationpy/tarball/0.10',
    version      = '0.10',
    packages     = ['durationpy'],
    package_data = {'durationpy': ['py.typed', '*.pyi']},
    license      = 'MIT'
)
