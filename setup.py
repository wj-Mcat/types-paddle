"""
setup
"""
from imaplib import Commands
import os
from typing import List

import semver
import setuptools


def versioning(version: str) -> str:
    """
    version to specification

    X.Y.Z -> X.Y.devZ

    """
    sem_ver = semver.parse(version)

    major = sem_ver['major']
    minor = sem_ver['minor']
    patch = str(sem_ver['patch'])

    if minor % 2:
        patch = 'dev' + patch

    fin_ver = '%d.%d.%s' % (
        major,
        minor,
        patch,
    )

    return fin_ver


def get_version() -> str:
    """
    read version from VERSION file
    """
    version = '0.0.0'

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'VERSION'
            )
    ) as version_fh:
        # Get X.Y.Z
        version = version_fh.read().strip()
        # versioning from X.Y.Z to X.Y.devZ
        version = versioning(version)

    return version


def get_long_description() -> str:
    """get long_description"""
    with open('README.md', 'r') as readme_fh:
        return readme_fh.read()


def get_install_requires() -> List[str]:
    """get install_requires"""
    with open('requirements.txt', 'r') as requirements_fh:
        return requirements_fh.read().splitlines()

setuptools.setup(
    name='types-paddle',
    version=get_version(),
    author='Jingjing WU (吴京京)',
    author_email='wujingjing05@baidu.com',
    description='type stub files for paddle to make tensor more intelligence in IDE',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    license='Apache-2.0',
    url='https://github.com/wj-Mcat/types-paddle',
    packages=['types_paddle'],
    include_package_data=True,
    package_data={
        "types_paddle": ["**/*.py", "**/*.pyi"]
    },
    
    # install_requires=get_install_requires(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'types-paddle = types_paddle.cli:main'
        ]
    }
)
