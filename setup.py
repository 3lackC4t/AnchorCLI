from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
with open('requirements.txt', 'r', encoding='utf-8') as fh:
    requirements = fh.read()

setup (
    name = "main",
    version = "0.0.1",
    author = "Cameron Minty",
    author_email = "C.S.Minty@proton.me",
    license = 'GNU General Public License',
    description = 'Manage shortcuts to directories in order to quickly navigate a filesystem',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/3lackC4t/AnchorCLI.git',
    packages = ['src'], 
    install_requires = [requirements],
    python_requires = '>=3.7',
    classifiers = [
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'ancr = src.application:main'
        ],
    },
    )
