from setuptools import setup, find_packages

PACKAGE_NAME = 'pyswell'
VERSION = '0.0.1'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author='',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'requests',
        'requests_toolbelt',
        'ratelimit'
    ]
)