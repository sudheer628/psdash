# coding=utf-8
from psdash import __version__
from setuptools import setup, find_packages

setup(
    name='psdash',
    version=__version__,
    description='Linux system information web dashboard',
    long_description='psdash is a system information web dashboard for linux using data mainly served by psutil',
    classifiers=[
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
        'Topic :: System :: Networking :: Monitoring',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'License :: Public Domain',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
    ],
    keywords='linux web dashboard',
    author='Joakim Hamrén, Sudheer628',
    author_email='sudheer628@yahoo.com',
    url='https://github.com/sudheer628/psdash',
    license='CC0',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.1.0',
        'psutil==2.1.3',
        'glob2==0.4.1',
        'gevent==1.4.0',
        'zerorpc==0.6.3',
        'netifaces==0.10.4',
        'argparse'
    ],
    test_suite='tests',
    tests_require=['unittest2'],
    entry_points={
        'console_scripts': [
            'psdash = psdash.run:main'
        ]
    }
)
