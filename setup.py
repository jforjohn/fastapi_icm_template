from setuptools import setup, find_packages


setup(
    name="icm",
    version="0.0.1",
    description="I.C.M",
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "icm = icm.__main__:cli",
        ]
    },
)
