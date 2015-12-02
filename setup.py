"""
Created on 24/gen/2014

@author: Marco Pompili
"""

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name=str('django-instagram'),
    version=str('0.1.1'),
    packages=['django_instagram', 'django_instagram.templatetags'],
    include_package_data=True,
    license=str('BSD-3 License'),
    description=str('Instagram client for Django.'),
    long_description=README,
    url=str('https://github.com/marcopompili/django-instagram'),
    author=str('Marco Pompili'),
    author_email=str('marcs.pompili@gmail.org'),
    install_requires=['django>=1.6', 'python-instagram'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
