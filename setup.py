import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())

setup(
    name="useless",
    version='1.1.0',
    url="https://github.com/nogoodusername/py-useless-package",

    author="KN",
    author_email="kshitij.nagvekar@workindia.in",

    description="This is an example package d",
    long_description=read("README.md"),

    packages=find_packages(exclude=('tests',)),

    install_requires=[
        "Django",
        "workindia-basemodels",
        "workindia-generic-adapter"
    ],
    setup_requires=[
        'wheel',
        'pip>=20'
    ],
    python_requires='>=3.6',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent"
    ],
)