"""The setup py file is an essential part of packaging and
distributing Python projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more"""

from setuptools import setup, find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """This function will return the list of requirements"""
    requirement_list:List[str]=[]
    try:
        with open("requirements.txt","r") as requirement_file:
            #read lines from file
            lines = requirement_file.readlines()
            #process each line to remove whitespace and newlines
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_list

print(get_requirements())

setup(
    name="Network Security Project",
    version="0.1",
    author="Huzaifa",
    packages=find_packages(),
    install_requires=get_requirements(),
)
    