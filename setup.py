from setuptools import setup, find_packages
import os
import pathlib


HERE = pathlib.Path(__file__).parent
README = (HERE / "readme.md").read_text()
HISTORY = (HERE / "history.md").read_text()

VERSION = '0.1.14'
DESCRIPTION = 'Simple Python Library to generate random usernames for websites.'
LONG_DESCRIPTION = README + '\n\n' + HISTORY

# Setting up
setup_args = dict(
    name="uugenerator",
    version=VERSION,
    author="Ali Mulla",
    author_email="<alimulla81@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'username', 'username generator', 'generator', 'ultimate'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

install_requires=[
    'importlib-resources'
]

if __name__== '__main__':
    setup(**setup_args, 
    install_requires=install_requires,
    include_package_data=True
    )
