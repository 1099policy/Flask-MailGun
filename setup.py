#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask-MailGun3
Flask extension to use the Mailgun email parsing service
for sending and receving emails
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Compatibility shim for setuptools 71+ with old packaging < 22.0
try:
    import packaging.utils
    import inspect

    _orig_canonicalize = packaging.utils.canonicalize_version
    if "strip_trailing_zero" not in inspect.signature(_orig_canonicalize).parameters:

        def _compat_canonicalize(version, strip_trailing_zero=True):
            return _orig_canonicalize(version)

        packaging.utils.canonicalize_version = _compat_canonicalize
except Exception:
    pass

with open("Version", encoding="utf-8") as f:
    version = next(f).strip()

# Ensure version is a valid PEP 440 version string
if not version:
    raise ValueError("Version file is empty")

with open("README.rst", encoding="utf-8") as f:
    readme = f.read()

# Read requirements from requirements.txt
requirements = []
try:
    with open("requirements.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                requirements.append(line)
except FileNotFoundError:
    pass

__NAME__ = "Flask-MailGun"
__doc__ = readme
__author__ = "Amey-SAM"
__license__ = "MIT"
__copyright__ = "2016"

setup(
    name=__NAME__,
    version=version,
    license=__license__,
    description="Flask extension to use the Mailgun email parsing service",
    long_description=__doc__,
    author=__author__,
    author_email="richard.mathie@amey.co.uk",
    url="https://github.com/1099policy/Flask-MailGun",
    download_url="https://github.com/1099policy/Flask-MailGun/tarball/master",
    # py_modules=['flask_mailgun'],
    packages=["flask_mailgun"],
    install_requires=requirements,
    keywords=["flask", "mailgun"],
    zip_safe=False,
    platforms="any",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
