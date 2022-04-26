from setuptools import find_packages, setup
from ad_attrib import __version__

setup(
    name="ad_attrib",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
