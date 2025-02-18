from setuptools import setup, find_packages


setup(
    name="geoloc_util",
    version="0.1.0",
    author="Richa Agrawal",
    author_email="richa.jss@gmail.com",
    description="A utility for getting geographical information for locations",
    url="https://github.com/richa-agarwal/geoloc-util",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    extras_require={
        "test": ["pytest"],
    },
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "geoloc-util=geoloc_util.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)