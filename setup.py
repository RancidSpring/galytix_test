from setuptools import setup, find_packages

setup(
    name="galytix_project",
    version="0.1.0",
    description="Galytix test project",
    author="Lev Kisselyov",
    author_email="levkiselev2000@gmail.com.com",
    packages=find_packages(),
    install_requires=[
        "toml~=0.10.2",
        "gensim~=4.3.3",
        "pandas~=2.2.2",
        "numpy~=1.26.4",
        "nltk~=3.9.1",
        "fuzzymatcher~=0.0.6",
        "scikit-learn~=1.5.1",
        "tabulate~=0.9.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
