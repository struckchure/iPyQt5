import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iPyQt5",
    version="0.0.1",
    author="Mohammed Al Ameen Bolutife",
    author_email="ameenmohammed2311@gmail.com",
    description="Desktop UI library based on Qt5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohammed2702/iPyQt5",
    project_urls={
        "Bug Tracker": "https://github.com/mohammed2702/iPyQt5/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"iPyQt5": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
