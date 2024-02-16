from setuptools import find_packages, setup
from typing import List

EQUIREMENTS_FILE_NAME ="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->list[str]:
    with open(EQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirements_name.replace("\n","") for requirements_name in requirement_list]    

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)

    return requirement_list


setup(
    name = "cost prediction",
    version="0.0.1",
    description="data science projects",
    author="susheela kothakonda",
    author_email="sushe9sushe@gmail.com",
    packages = find_packages(),
    install_requires= get_requirements(),
    )

