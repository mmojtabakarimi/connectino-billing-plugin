#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-billing',
    version='1.0',
    description='Connectino billing plugin',
    author='Mojtaba Karimi',
    author_email='mmojtabakarimi@yahoo.com',
    packages=find_packages(),
    url='https://www.foo-bar.com',
    include_package_data=True,
    package_data={
        'wazo_confd_billing': ['api.yml'],
    },

    entry_points={
        'wazo_confd.plugins': [
            'billing = wazo_confd_billing.plugin:Plugin'
        ]
    }
)
