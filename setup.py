from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="FrogCord",
    version="1.0",
    author="Stephanie Phillips",
    description="A custom suite of helpful classes and utilities for working on Discord Bots with PyCord.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AllegroVivo/FrogCord",
    packages=find_packages(),
    install_requires=[
        "psycopg2 ~= 2.9.7",
        "py-cord ~= 2.4.1"
    ],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
################################################################################
