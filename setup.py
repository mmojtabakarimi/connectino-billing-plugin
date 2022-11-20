#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-survey',
    version='1.0',
    description='Connectino survey plugin',
    author='Mojtaba Karimi',
    author_email='mmojtabakarimi@yahoo.com',
    packages=find_packages(),
    url='https://www.foo-bar.com',
    include_package_data=True,
    package_data={
        'wazo_confd_survey': ['api.yml'],
    },

    entry_points={
        'wazo_confd.plugins': [
            'survey = wazo_confd_survey.plugin:Plugin'
        ]
    }
)
