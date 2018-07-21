#!/usr/bin/env python
import os
from setuptools import setup, find_packages


# https://packaging.python.org/guides/single-sourcing-package-version/
version = {}
with open(os.path.join("src", "astrool", "__init__.py")) as fp:
    exec(fp.read(), version)


# http://blog.ionelmc.ro/2014/05/25/python-packaging/
setup(
    name="astrool",
    version=version['__version__'],
    description="Python package for Astronomers in a Hurry",
    author="Shreyas Bapat",
    author_email="contact@shreyasb.com",
    url="http://shreyasb.com/",
    download_url="https://github.com/shreyasbapat/astrool",
    license="MIT",
    keywords=[
        "astro", "positional", "astronomy",
        "ephem", "orbits", "every-astro", "orbital mechanics"
    ],
    python_requires=">=3.5",
    install_requires=[
        "numpy",
        "astropy>=3.0,<4.*",
        "matplotlib>=2.0",
        "ephem",
        "scipy",
        "beautifulsoup4>=4.5.3",
        "requests",
        "pandas",
        "plotly>=3.0,<4.*",
        "astroquery>=0.3.8",
    ],
    extras_require={
        ':implementation_name=="cpython"': "numba>=0.39",
        'dev': [
            "coverage",
            "pytest-cov",
            "pycodestyle",
            "sphinx",
            "sphinx_rtd_theme",
            "nbsphinx",
            "ipython>=5.0",
            "jupyter-client",
            "ipykernel",
            "ipywidgets",
        ]
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'astrool = astrool.cli:main'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    long_description=open('README.rst', encoding='utf-8').read(),
    include_package_data=True,
    zip_safe=False,
)
