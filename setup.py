import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cryptounifier',
    version='1.0.1',
    description='CryptoUnifier API Python Integration.',
    url='https://cryptounifier.io/',
    author='https://cryptounifier.io/',
    license='MIT License',
    packages=['cryptounifier'],
    install_requires=['requests'],

    url="https://github.com/cryptounifier/python-sdk",
    project_urls={
        "Bug Tracker": "https://github.com/cryptounifier/python-sdk/issues",
    },

    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)