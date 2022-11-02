"""
Butler Doc AI SDK
"""
from setuptools import find_packages, setup

NAME = "docai"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "attrs>=21.3.0",
    "httpx>=0.15.4,<0.24.0",
    "pdf2image",
    "pillow",
    "python-dateutil~=2.8.1",
    "typing_extensions",
]

setup(
    name=NAME,
    version=VERSION,
    description="Butler Doc AI",
    author="Butler Labs",
    author_email="support@butlerlabs.ai",
    url="https://butlerlabs.ai",
    project_urls={"Documentation": "https://docs.butlerlabs.ai/reference/welcome"},
    keywords=["Butler", "AutoML", "OCR"],  # TODO
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
           Welcome to Butler Document AI
    """,
)
