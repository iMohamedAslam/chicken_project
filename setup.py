from setuptools import find_packages, setup

setup(
    name='chicken',
    version='0.0.0',
    author='Bappy',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[]
)