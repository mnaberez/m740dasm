__version__ = '1.0.0.dev0'

import sys
from setuptools import setup, find_packages

if sys.version_info[:2] < (3, 8):
    raise RuntimeError('m740dasm requires Python 3.8 or later')

DESC = "Renesas (Mitsubishi) 740 disassembler"

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Assembly',
    'Topic :: Software Development :: Disassemblers',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: System :: Hardware'
]

setup(
    name='m740dasm',
    version=__version__,
    license='License :: OSI Approved :: BSD License',
    url='',
    description=DESC,
    long_description=DESC,
    classifiers=CLASSIFIERS,
    author="Mike Naberezny",
    author_email="mike@naberezny.com",
    maintainer="Mike Naberezny",
    maintainer_email="mike@naberezny.com",
    packages=find_packages(),
    install_requires=[],
    extras_require={},
    include_package_data=True,
    zip_safe=False,
    test_suite="m740dasm.tests",
    entry_points={
        'console_scripts': [
            'm740dasm = m740dasm.command:main',
        ],
    },
)
