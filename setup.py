from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='interaction',
	version='1.0.4',
	description='Python library for creating progress bars',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/idin/interaction',
	author='Idin',
	author_email='py@idin.ca',
	license='MIT',
	packages=find_packages(exclude=("jupyter_tests", ".idea", ".git")),
	install_requires=['pandas'],
	python_requires='~=3.6',
	zip_safe=False
)
