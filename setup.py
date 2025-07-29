from setuptools import setup, find_packages

setup(
    name='webscraper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'webscraper=webscraper.cli:main'
        ]
    },
    author='Your Name',
    description='Reusable Python Web Scraper Package'
)