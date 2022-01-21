import os

from setuptools import setup


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="specification",
    version="0.0.1",
    description="Digital Land specifications, built upon the GOV.UK Registers data model.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="MHCLG Digital Land Team",
    author_email="DigitalLand@communities.gov.uk",
    license="MIT",
    url="https://github.com/digital-land/specification",
    packages=["specification"],
    package_data={
        "digital_land/specification": ["specification/*"],
        "specification": ["specification/*"],
    },
    include_package_data=True,
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
