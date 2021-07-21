import pathlib
from setuptools import setup, find_packages

# The directory contianing this file
HERE = pathlib.Path(__file__).parent

# The text of the readme file
README = (HERE / "readme.md").read_text()
#LICENCE=(HERE / "LICENCE").read_text()
# This call to setup does all the work

setup(
    name="ultimate-username-generator",
    version="0.0.3",
    description="A username generator that generates based on user chosen lists",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bitFez/UltimateUserNameGenerator",
    py_modules=["uugenerator"],
    packages=find_packages(),
    packages_dir={'', 'src'},
    author="Ali Mulla",
    licence="LICENCE",
    include_data_package=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=['username', 'username generator', 'generate', 'usernames'],
)