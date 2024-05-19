from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str) -> List[str] :
    '''
    Returns a list of the requirements.txt folder
    '''

    requirements = []
    with open('requirements.txt') as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("/n", " ") for req in requirements]

    return requirements


setup(
    name='matrix factorization',
    version='0.0.1',
    author='Zhanna',
    author_email='orlova.zhan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

