from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='Ml_Project',
    version='0.0.1',
    description='End_to_End_ML_Project',
    author='Ashira Maharjan',
    author_email='ashiramaharjan13@gmail.com',
    packages=find_packages(), # Automatically discover and include all packages
    # install_requires=['pandas', 'numpy', 'seaborn']
    install_requires=get_requirements('requirements.txt')
    # Other potential arguments: long_description, license, url, entry_points
)