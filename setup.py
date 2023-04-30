import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AIOPools",
    version="0.1.0",
    author="Cyberbolt",
    author_email="dtconlyone@gmail.com",
    description="AIOPools is a lightweight library for building Python AsyncIO coroutine pools. | AIOPools 是一个轻量级的用于构建 Python AsyncIO 协程池的库。",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[]    
)