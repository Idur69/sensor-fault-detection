from setuptools import find_packages, setup 
from typing import List

def get_requirments()->List[str]:
    """
    This function will return list of requirements

    Returns:
        List[str]: _description_
    """
    requirements_list : List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="idur",
    author_email="shaikidurbasha469@gmail.com",
    package=find_packages(),
    install_requires=get_requirments(),#"pymongo==4.2.0",
)