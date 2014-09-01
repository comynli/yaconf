
from setuptools import setup, find_packages

def readme():
        with open("README.rst") as f:
                    return f.read()

setup(
    name='yaconf',
    version="0.1",
    license='BSD-3',
    author='comyn',
    author_email='me@xueming.li',
    description='Wrapper yaml config files.',
    long_description=readme(),
    url='https://github.com/lixm/yaconf',
    install_requires=[
        "PyYAML >= 3.1",
    ],
    packages=['yaconf'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        ],
    )
