from setuptools import setup, find_packages

setup(
    name='my_spark_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyspark==3.1.2'
    ],
)