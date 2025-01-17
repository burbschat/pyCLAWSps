from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="c11204ps",
    version="0.2.0",
    description="Python package for controlling a Hamamatsu c11204-01/02 power supply",
    long_description=readme(),
    keywords=["hamamatsu", "power supply", "c11204", "c11204-01", "c11204-02"],
    url="https://github.com/burbschat/pyCLAWSps",
    author="Bela Urbschat",
    author_email="b.urbschat@tum.de",
    license="gpl-3.0",
    packages=["pyCLAWSps"],
    install_requires=["pySerial"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
