from setuptools import setup, find_packages

with open("README_PUBLIC.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    
    name="image_processing",
    version="0.0.1",
    author="Wagner Andrade",
    description="A package to process images",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wsawebmaster/python-image-processing",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6",
)