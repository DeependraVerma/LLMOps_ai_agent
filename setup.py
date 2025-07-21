from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(

    name = "MULTI-AI AGENTS",
    version = "0.1",
    author = "Deependra",
    packages=find_packages(),
    install_requires = requirements
)

