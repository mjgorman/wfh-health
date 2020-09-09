#!/usr/bin/env python
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='wfm-health',
    version='0.1.0',
    description="Notifications for more healthy behavior.",
    long_description="Work from home healthy notifications to guide you into a more healthy working structure throughout your day",
    author="Michael J. Gorman",
    author_email='michael@michaeljgorman.com',
    url='https://github.com/mjgorman/wfh-health',
    license='MIT',
    install_requires=required
    entry_points={
        'console_scripts': [
            'wfm-health = wfh-health.__main__:app',
        ],
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
