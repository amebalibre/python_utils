"""Setup file."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amebalibre_utils",
    version="0.0.1",
    author="Amebalibre",
    author_email="vai@mailbox.org",
    description="Personal utilities classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amebalibre/python_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3",
        "Operating System :: OS Independent",
    ],
)
