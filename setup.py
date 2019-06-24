from setuptools import setup, find_packages

setup(
    name='Nightintale',
    version='0.0.1',
    description='Discord Hack Week',
    author='Lucas Bares',
    author_email='lucasbaresm@gmail.com',
    url='https://github.com/LucasBares/Nightingale',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)