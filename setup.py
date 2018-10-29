#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['click>=6.0', 'requests', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Kevin P. Fleming",
    author_email='kevin+py@km6g.us',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
    ],
    description="A simple tool to deploy TLS certificates obtained using Certbot to FreeNAS systems.",
    entry_points={
        'console_scripts': [
            'certbot_freenas_deployer=certbot_freenas_deployer.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='certbot freenas',
    name='certbot_freenas_deployer',
    packages=find_packages(include=['certbot_freenas_deployer']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kpfleming/certbot_freenas_deployer',
    version='1.1.0',
    zip_safe=False,
    python_requires='>=3.5',
)
