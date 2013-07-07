import os
import sys

from setuptools import find_packages, setup
# DISABLED, use VERSION.txt now: from behave.version import VERSION
VERSION = open("VERSION.txt").read().strip()

if "TRAVIS_BUILD_ID" in os.environ:
    # -- SAD: TRAVIS-CI only supports distribute 8-(
    requirements = ['parse>=1.6.2', 'distribute']
else:
    requirements = ['parse>=1.6.2', 'setuptools>=0.7.5']

zip_safe = True
major, minor = sys.version_info[:2]
if major == 2 and minor < 7:
    requirements.append('argparse')
    requirements.append('importlib')
if major == 2 and minor < 6:
    requirements.append('simplejson')

description = ''.join(open('README.rst').readlines()[5:])

setup(
    name='behave',
    version=VERSION,
    description='behave is behaviour-driven development, Python style',
    long_description=description,
    author='Benno Rice, Richard Jones and Jens Engel',
    author_email='behave-users@googlegroups.com',
    url='http://github.com/behave/behave',
    packages=find_packages(exclude=["test", "test.*"]),
    entry_points={
        'console_scripts': ['behave = behave.__main__:main'],
    },
    install_requires=requirements,
    use_2to3=True,
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: BSD License",
    ],
)
