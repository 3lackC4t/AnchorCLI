#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
        name="AnchorCLI",
        version="0.1",
        packages=find_packages(),
        entry_points={
            "console_scripts": [
                    "anc=AnchorCLI.__main__:main",
                ]
            }
        )
