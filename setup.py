# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup

project_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(project_dir, 'README.rst'), 'r') as f:
    long_description = f.read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='python-evrythng',
    version='0.3.5',
    packages=['evrythng', 'evrythng.entities', 'evrythng.extended'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/GooeeIOT/python-evrythng',
    license='MIT',
    author='Gooee LLC',
    author_email='lyle@gooee.com',
    description='A comprehensive pythonic wrapper around the Evrythng REST API.',
    long_description=long_description,
    install_requires=['requests>=2.8.1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries'
    ],
    keywords=['wrapper', 'iot', 'rest', 'api', 'evrythng', 'client', 'internet of things', 'thng'],
)
