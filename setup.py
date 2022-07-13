from pathlib import Path
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def glob_fix(package_name, glob):
    # this assumes setup.py lives in the folder that contains the package
    package_path = Path(f'./{package_name}').resolve()
    return [str(path.relative_to(package_path)) 
            for path in package_path.glob(glob)]

setuptools.setup(
    name='ergo_python_appkit',  
    version='0.2.1',
    packages=['ergo_python_appkit'] ,
    author="Robert Pieter van Leeuwen",
    author_email="luivatra@gmail.com",
    description="A python wrapper for the Ergo Appkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ergo-pad/ergo-python-appkit",
    package_data={'ergo_python_appkit': [*glob_fix('ergo_python_appkit', 'typings/**/*'),'jars/*.jar']},
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