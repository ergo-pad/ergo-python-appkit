import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='ergo_python_appkit',  
    version='0.0.2',
    packages=['ergo_python_appkit'] ,
    author="Robert Pieter van Leeuwen",
    author_email="luivatra@gmail.com",
    description="A python wrapper for the Ergo Appkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ergo-pad/ergo-python-appkit",
    package_data={'ergo_python_appkit': ['jars/*.jar']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'jpype1',
    ]
 )