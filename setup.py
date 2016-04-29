# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

project_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(project_dir, 'src/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

with open(os.path.join(project_dir, 'README.rst'), 'r') as f:
    long_description = f.read()

setup(
    name='python-evrythng',
    version=version,
    packages=find_packages(exclude=["docs", "tests*"]),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/GooeeIOT/python-evrythng',
    license='MIT',
    author='Gooee, Inc',
    author_email='lyle@gooee.com',
    maintainer='Dairon Medina',
    maintainer_email='dairon@gooee.com',
    description='A Python wrapper arround the Evrythng REST API.',
    long_description=long_description,
    install_requires=['requests>=2.8.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries'
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='Wrapper IoT REST API Evrythng',
)
