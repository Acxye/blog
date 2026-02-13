from setuptools import setup

setup(
    name="mytools",
    version="0.1.0",
    py_modules=["concatenate_img"],
    entry_points={
        "console_scripts": [
            "concatenate_img=concatenate_img:main",
        ],
    },
)
