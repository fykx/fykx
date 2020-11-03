import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fykx",
    version="0.0.1",
    author="Jianbang Wang",
    author_email="iayden_fykx@outlook.com",
    description="Geographic data processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fykx/fykx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)