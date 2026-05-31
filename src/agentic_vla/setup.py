from glob import glob
import os

from setuptools import find_packages, setup

package_name = "agentic_vla"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml", "README.md"]),
        (os.path.join("share", package_name, "config"), glob("config/*.yaml")),
        (os.path.join("share", package_name, "launch"), glob("launch/*.py")),
        (os.path.join("share", package_name, "scripts"), glob("scripts/*.sh")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="student",
    maintainer_email="todo@todo.com",
    description="Scenario assets and launch helpers for the Agentic VLA final lab.",
    license="MIT",
    entry_points={"console_scripts": []},
)
