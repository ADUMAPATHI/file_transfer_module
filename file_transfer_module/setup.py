from setuptools import setup, find_packages

setup(
    name='file-transfer-module',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'boto3',  # AWS SDK for Python
        'google-cloud-storage'  # Google Cloud Storage client library
    ],
)
