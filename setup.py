import glob
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    README = readme_file.read()

REQUIREMENTS = [
    "packaging",
    "numpy",
    "matplotlib",
    "setuptools_scm",
    "qtpy",
    "PySide2",
]

setup(
    name="CoatingGUI",
    use_scm_version={
        "write_to": "gui/_version.py",
    },
    description = "Graphical user interface for designing dielectric mirror coatings",
    long_description=README,
    author="Sebastian Steinlechner, Sean Leavey",
    package_data={
        "gui": [
            "*.ui",
            "*.ico",
            "*.svg",
        ]
    },
    install_requires=REQUIREMENTS,
    setup_requires=["setuptools_scm"],
)
