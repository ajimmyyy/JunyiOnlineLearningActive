from setuptools import setup, find_packages

setup(
    name='SelectFrequentItems',
    version='0.1',
    author='jimmy',
    description='Select frequent item sets',
    packages = find_packages(),
    install_requires=[
        "pandas",
        'numpy',
        "mlxtend",
        "matplotlib",
        "tqdm",
    ],
)
