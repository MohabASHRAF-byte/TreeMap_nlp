from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Tree Bank Map'

# Setting up
setup(
    name="vidstream",
    version=VERSION,
    author="Mohab",
    author_email="<a.mohab148@@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['nltk'],
    classifiers=[
        "Development Status :: 1 - Development",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)