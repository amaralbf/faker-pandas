from setuptools import setup

setup(
    name='pandas-faker',
    version='0.1.0',
    description='',
    long_description=None,
    author='Bruno Amaral',
    author_email='amaralbf@gmail.com',
    package_dir={'': 'src'},
    packages=['pandas_faker'],
    python_requires='>=3.6,<4.0',
    install_requires=['pandas'],
)
