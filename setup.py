from setuptools import setup, find_packages

# Leer las dependencias desde requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    required = f.read().splitlines()

setup(
    name='CoderHouse_57810',
    version='1.0.0',
    description='Sistema de gestión para CoderHouse',
    author='Ginette Laglere',
    author_email='glaglere@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    entry_points={
        'console_scripts': [
            'coderhouse_57810 = CoderHouse_57810.main:main',
        ],
    },
)
