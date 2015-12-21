try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='python-evrythng',
    version='0.1',
    packages=['evrythng', 'evrythng.entities'],
    package_dir={'': 'src'},
    url='https://github.com/GooeeIOT/python-evrythng',
    license='MIT',
    author='Lyle Scott, III',
    author_email='lyle@digitalfoo.net',
    description='A Python wrapper about the Evrythng REST API.'
)
