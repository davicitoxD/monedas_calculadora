from setuptools import setup, find_packages

from os import path

project_folder = path.abspath(path.dirname(__file__))

_version = __import__("dolarconverter").__version__

setup(
    name="dolarconverter",
    version=_version,
    author="David Runke",
    author_email="davidrunke@gmail.com",
    packages=find_packages(),
    description="conversor online de pesos a dolares",
    url="https://github.com/davicitoxD/monedas_calculadora.git",
    license=None,
    long_description_content_type="text/markdown",
    
)