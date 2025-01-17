"""
{{ cookiecutter.python_name }} setup
"""
import json
import sys
from pathlib import Path

import setuptools

HERE = Path(__file__).parent.resolve()

# Get the package info from package.json
pkg_json = json.loads((HERE / "package.json").read_bytes())

# The name of the project
name = "{{ cookiecutter.python_name }}"

quetz_path = (HERE / pkg_json["quetz"]["outputDir"])

# Representative files that should exist after a successful build
ensured_targets = [
    str(quetz_path / "package.json"){% if cookiecutter.kind.lower() != "theme" %},
    str(quetz_path / "static/style.js"){% endif %}
]

quetzext_name = pkg_json["name"]

data_files_spec = [
    ("share/quetz/frontend/extensions/%s" % quetzext_name, str(quetz_path.relative_to(HERE)), "**"),
    ("share/quetz/frontend/extensions/%s" % quetzext_name, str("."), "install.json")
]

long_description = (HERE / "README.md").read_text(encoding="utf8")

version = (
    pkg_json["version"]
    .replace("-alpha.", "a")
    .replace("-beta.", "b")
    .replace("-rc.", "rc")
)

setup_args = dict(
    name=name,
    version=version,
    url=pkg_json["homepage"],
    author=pkg_json["author"]["name"],
    author_email=pkg_json["author"]["email"],
    description=pkg_json["description"],
    license=pkg_json["license"],
    license_file="LICENSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["quetz-frontend"],
    extras_require={
        "test": [{% if cookiecutter.test.lower().startswith('y') %}
            "coverage",
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
            "pytest-tornasync"
        {% endif %}]
    },
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.7",
    platforms="Linux, Mac OS X, Windows",
    keywords=["Quetz"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
)

try:
    from jupyter_packaging import (
        wrap_installers,
        npm_builder,
        get_data_files
    )
    post_develop = npm_builder(
        build_cmd="install:extension", source_dir="src", build_dir=quetz_path
    )
    setup_args["cmdclass"] = wrap_installers(post_develop=post_develop, ensured_targets=ensured_targets)
    setup_args["data_files"] = get_data_files(data_files_spec)
except ImportError as e:
    import logging
    logging.basicConfig(format="%(levelname)s: %(message)s")
    logging.warning("Build tool `jupyter-packaging` is missing. Install it with pip or conda.")
    if not ("--name" in sys.argv or "--version" in sys.argv):
        raise e

if __name__ == "__main__":
    setuptools.setup(**setup_args)
