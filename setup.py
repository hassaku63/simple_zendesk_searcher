from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read()


setup(
    name='simple_zendesk_searcher',
    version='0.0.1',
    install_requires=requirements,
    description='CLI tool for search zendesk tickets',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='hassaku63',
    author_email='takuyahashimoto1988@gmail.com',
    # license='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Natural Language :: Japanese',
    ],
    keywords='zendesk',
    url='https://github.com/hassaku63/simple_zendesk_searcher',
    entry_points={
        'console_scripts': [
            'simple_zendesk_search = cli.zendesk_search:main'
        ]
    },
    packages=find_packages(exclude=['tests*']),
)
