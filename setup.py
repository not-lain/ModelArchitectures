import pathlib
from setuptools import find_packages, setup

setup(
    name="mymodels",
    version="0.0.1",
    description="a python package with basic architectures",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/not-lain/ModelArchitectures",
    Issues="https://github.com/not-lain/ModelArchitectures/issues",
    author= "hafedh hichri",
    author_email="hhichri60@gmail.com",
    license="Apache 2.0 License",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    classifiers=["Topic :: Utilities", "Programming Language :: Python :: 3.9"],
    requires=["setuptools", "wheel"],
)
