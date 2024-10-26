from setuptools import setup, find_packages

setup(
    name="imgtool",
    version="1.0.0",
    description="An advanced image processing tool using OpenCV",
    author="Raj Acharya",
    author_email="razzacharya670@gmail.com",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "exifread"
    ],
    entry_points={
        "console_scripts": [
            "imgtool=imgtool.image_processor:ImageProcessor",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
