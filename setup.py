from setuptools import find_packages, setup

with open("app/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="ln.py.core",
    version="1.0.0",
    description="Core Python Library",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/github-lernender-corp/ln.py.core",
    author="Lovelidge, Shawn",
    author_email="slovelidge@lernendercorp.com",
    license="MIT",
    keywords=['python', 'core'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10", "uuid >= 1.30", "uuid64 >= 0.2.0"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.11",
)