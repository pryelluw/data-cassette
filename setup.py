from setuptools import setup, find_packages

setup(
    name='Data Cassette',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    install_requires=['pyyaml'],
    url='https://github.com/pryelluw/data-cassette',
    author='Pablo Rivera',
    author_email='pr@tinytiny.app'
)