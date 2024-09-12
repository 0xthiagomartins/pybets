from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pybets",
    version="0.1.0",
    author="Thiago Martins",
    author_email="martins@dmail.ai",
    description="Python package for Brazilian Economic Time Series",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0xthiagomartins/pybets",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "polars",
        # Add other dependencies as needed
    ],
)
