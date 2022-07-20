from setuptools import setup

setup(
    name="mongotocsv",
    version="0.1.3",
    description="Creates a CSV file from a MongoDB collection",
    url="https://github.com/BlackIsBlack/mongotocsv",
    author="Cameron Jensen",
    author_email="cameron@situ.com.au",
    license="BSD 2-clause",
    packages=["mongotocsv"],
    install_requires=["pandas", "pymongo"],
    classifiers=["Programming Language :: Python :: 3.10"],
)
