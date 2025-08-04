from setuptools import setup, find_packages

setup(
    name="afsar_pipeline",
    version="0.1.0",
    author="Afsar Basha",
    author_email="bafsar67@gmail.com",
    description="A Python toolkit for daily ETL and pipeline tasks",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Afsar6786/afsar_pipeline",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "pyspark>=3.0.0"
    ],
    python_requires=">=3.7",
)