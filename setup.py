# coding=utf-8
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='webassets-libsass',
    version='0.1',
    description='Filter for asset management "webassets" that uses "libsass"',
    url='https://bitbucket.org/jhuss/webassets-libsass',
    author='Jesús Jerez',
    author_email='jerezmoreno@gmail.com',
    license='BSD',
    install_requires=[
        'libsass',
        'webassets'
    ],
    packages=['webassets_libsass'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ]
)
