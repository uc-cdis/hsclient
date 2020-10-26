from setuptools import setup

setup(
    name="hsclient",
    version="0.1",
    packages=[
        "hsclient",
    ],
    install_requires=[
        "requests>=2.5.2,<3.0.0",
    ],
)
