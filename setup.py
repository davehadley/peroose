from setuptools import setup

setup(name="peroose",
      version="0.1",
      description="A python-based command line tool to peruse ROOT files.",
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
      zip_safe=False,
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
