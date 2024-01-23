from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="panama-ruc-dv-calculator",
    version="1.0.1",
    author="Juan Corradine",
    description="A DV calculator for Panama RUC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juancorradine/panama-ruc-dv-calculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        # Add your package dependencies here
        # 'numpy', 'pandas', etc.
    ],
)
