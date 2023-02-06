from setuptools import setup
  
setup(
    name='sovereign',
    version='0.1',
    description='sovereign',
    author='mikatrust',
    author_email='mikatrust@example.com',
    packages=['sovereign'],
    install_requires=[
        'prettytables',
        'toverage',
	'pylint',
	'autopep8',
	'flake8',
	'pytest',
    ],
)
