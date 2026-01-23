from setuptools import find_packages,setup 
from typing import List

# create a function for requirements

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: Any

    this function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'ML_Project',
    version='0.0.1',
    author='Ashira',
    author_email='ashiramaharjan13@gmail.com',
    package=find_packages(),
    #install_requires=['pandas','numpy','seaborn'],
    install_requires=get_requirements('requirements.txt')
)