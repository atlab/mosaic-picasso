from setuptools import setup, find_packages

setup(
    name='mosaic_picasso',
    version='0.1.0',
    author='Hu Cang, Yang Liu, Jianhua Xing',
    author_email='hucang@gmail.com',
    description='Mosaic-PICASSO: accurate crosstalk removal for multiplex fluorescence imaging',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/atlab/mosaic-picasso',  # Repository URL
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=[],  # List of dependencies (can also be in requirements.txt)
    classifiers=[  # Optional metadata
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
