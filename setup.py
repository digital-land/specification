import os

from setuptools import find_packages, setup

#  from version import get_version


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="digital-land-specification",
    # TODO fix this
    #  version=get_version(),
    description="Digital Land specifications, built upon the GOV.UK Registers data model.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="MHCLG Digital Land Team",
    author_email="DigitalLand@communities.gov.uk",
    license="MIT",
    url="https://github.com/digital-land/specification",
    packages=["digital_land", "specification"],
    package_data={
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
