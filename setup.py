from setuptools import setup, find_packages

long_description = ""

setup(
    name="msk_cdm",
    version="0.1.0",
    description="Core MSK Clinical Data Mining group code.",
    url="https://github.com/clinical-data-mining/cdm-v2",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={  # Optional
        "console_scripts": [
            # can add executable entry points here.
        ],
    },
    python_requires=">=3.9, <4",
    install_requires=[
        "minio>=7.1,<8",
        "pydantic>=2.3,<3",
        "python-dotenv>=1.0,<2",
    ],
    extras_require={
        "dev": ["check-manifest"],
        "test": ["pyfakefs", "pytest", "tox"],
    },
)
