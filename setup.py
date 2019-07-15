#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-dynamic-subdomains',
    description="Dynamic and static subdomain support for Django.",
    version='1.3.0',
    url='https://chris-lamb.co.uk/projects/django-dynamic-subdomains/',

    author="Chris Adkins",
    author_email='c23gooey@gmail.com',
    license='BSD',

    packages=find_packages(),

    install_requires=(
        'Django>=2.2',
    ),
)
