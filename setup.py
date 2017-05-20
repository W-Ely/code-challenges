from setuptools import setup


setup(
    name='Katas',
    description="Code Wars Solutions with Tests",
    version='0.1',
    author="Ely",
    license='MIT',
    package_dir={'': 'src'},
    extras_require={'testing': ['pytest', 'pytest-cov', 'tox']}
)
