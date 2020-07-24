from setuptools import setup

with open("peroose/_version.py") as fp:
    version = {}
    exec(fp.read(), version)
    version = version["__version__"]

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(name="peroose",
      version=version,
      description="A python-based command line tool to peruse ROOT files.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/davehadley/peroose",
      author="David Hadley",
      author_email="d.r.hadley@warwick.ac.uk",
      license="MIT",
      packages=["peroose"],
      scripts=["bin/peroose"],
      install_requires=["ipython>=7.15.0"],
      extras_require={
          "uproot": "uproot>=3.11.7"
      },
      zip_safe=True,
      classifiers=[
          "Programming Language :: Python :: 3 :: Only",
          "License :: OSI Approved :: MIT License",
          "Development Status :: 2 - Pre-Alpha",
          "Operating System :: POSIX",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Physics",
      ],
      python_requires=">=3.6",
      )
