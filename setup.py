from setuptools import setup
from sys import platform

setup(name='git_commit',
        version='1.01d',
        description='Easily Standardize your github commit automatically!',
        url='https://github.com/jackofspades707/git-commit',
        author='JackofSpades707',
        author_email='JackofSpades707@hotmail.com',
        license='MIT',
        packages=['git_commit'],
        scripts=['git_commit/git_commit'],
        install_requires=['sh', 'argparse'],
        python_requires='>=3')
