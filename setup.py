from pathlib import Path
from setuptools import find_packages, setup

# Current directory
HERE = Path(__file__).resolve().parent

README = (HERE / "README.md").read_text()
DESC = ('Differentiable procedural material library based on PyTorch, supporting material graph '
        'translation and parameter optimization against user-input appearance captures')

REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.1.0'

# Run setup
setup(
    name='diffmat',
    version=VERSION,
    description=DESC,
    long_description=README,
    long_description_content_type="text/markdown",
    author='Beichen Li; Liang Shi',
    author_email='beichen@mit.edu; liangs@mit.edu',
    python_requires=REQUIRES_PYTHON,
    url="TODO",
    keywords='procedural material, differentiable computation, appearance modeling, SVBRDF map, '
             'gradient descent, optimization',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'numpy'
        'scipy',
        'imageio',
        'pandas',
        'pyyaml'
    ],
    include_package_data=True,
    license='Custom License',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Multimedia :: Graphics',
        'Intended Audience :: Product/Research',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
