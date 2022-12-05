from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='mycalc',
    version='0.0.1',  # Required
    description='Example calc package',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional
    author='Lele',  # Optional
    author_email='lele@yeye.com',  # Optional
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.6',
)
