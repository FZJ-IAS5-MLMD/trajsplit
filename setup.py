from setuptools import setup

setup(
    name='trajsplit',
    version='1.0',
    zip_safe=False,
    description='Python tool to split Gromacs trajectories and CPMD energy files to chunks.',
    author=["Bharath Raghavan"],
    author_email='b.raghavan@fz-juelich.de',
    packages=['trajsplit'],
    install_requires=['panedr'],
    entry_points = {
        'console_scripts': ['trajsplit = trajsplit.__main__:main'],
    })