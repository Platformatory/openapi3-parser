#!/usr/bin/env python

from os.path import dirname, join

from setuptools import find_packages, setup

#from src import openapi_parser

description_file = join(dirname(__file__), "readme.md")


__version__ = '1.1.8'
__title__ = 'openapi3-parser'
__author__ = 'Artem Manchenkov'
__email__ = 'artem@manchenkoff.me'
__description__ = 'OpenAPI v3 parser'

setup(
    name=__title__,
    author=__author__,
    author_email=__email__,
    url="https://github.com/manchenkoff/openapi3-parser",
    project_urls={
        "Source": "https://github.com/manchenkoff/openapi3-parser",
    },
    version=__version__,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    license="MIT",
    description=__description__,
    long_description=open(description_file).read(),
    long_description_content_type="text/markdown",
    keywords="swagger, python, swagger-parser, openapi3-parser, parser, openapi3, swagger-api",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        "prance>=0.20.2",
        "openapi-spec-validator==0.5.5",
    ],
)
