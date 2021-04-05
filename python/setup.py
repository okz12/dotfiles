from pathlib import Path

from setuptools import setup

import PKGNAME

BASE_DIR = Path(__file__).parent

# Load required packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# Load development packages from requirements-dev.txt
with open(Path(BASE_DIR, "requirements-dev.txt"), "r") as file:
    dev_packages = [ln.strip() for ln in file.readlines()]


setup(
    name="PKGNAME",
    version=PKGNAME.__version__,
    description="Package Desc",
    author="AUTHOR",
    url="PKGNAME.com",
    python_requires=">=3.6",
    install_requires=[required_packages],
    extras_require={
        "dev": required_packages + dev_packages,
    },
)
