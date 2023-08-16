from setuptools import find_packages, setup

with open("lib/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="ln.py.core",
    version="1.0.3",
    description="Core Python Library",
    package_dir={"": "lib"},
    packages=find_packages(where="lib"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/github-lernender-corp/ln.py.core",
    author="Lovelidge, Shawn",
    author_email="slovelidge@lernendercorp.com",
    license="MIT",
    keywords=['python', 'core', 'machine', 'learning', 'ml', 'ai'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=["uuid >= 1.30", "uuid64 >= 0.2.0"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.11",
)