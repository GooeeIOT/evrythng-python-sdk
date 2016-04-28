try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='python-evrythng',
    version='0.2',
    packages=['evrythng', 'evrythng.entities'],
    package_dir={'': 'src'},
    url='https://github.com/GooeeIOT/python-evrythng',
    license='MIT',
    author='Gooee, Inc',
    author_email='lyle@gooee.com',
    description='A Python wrapper about the Evrythng REST API.',
    install_requires=[
        'requests',
    ],
)
