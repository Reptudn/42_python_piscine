from setuptools import setup, find_packages

"""
setup.py is a script that helps you to distribute
your Python application.
"""
setup(
    name="ft_package",
    version="1.0.0",
    packages=find_packages(),
    author="jkauker",
    author_email="jkauker@student.42heilbronn.de",
    description="dont bother using it",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Reptudn/42_python_piscine/tree/main/Python00/ex09",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
