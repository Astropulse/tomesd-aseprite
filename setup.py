from setuptools import find_packages, setup

setup(
    name="tomesd",
    version="0.1.4",
    author="Daniel Bolya & Cody Claus",
    url="https://github.com/Astropulse/tomesd-aseprite/",
    description="Token Merging for Stable Diffusion, fixed for split model architecture",
    install_requires=["torch>=1.12.1"],
    packages=find_packages(exclude=("examples", "build")),
    license = 'MIT',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)
