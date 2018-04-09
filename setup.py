"""
Created on 24/gen/2014

@author: Marco Pompili
"""

import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name=str('django-instagram'),
    version=str('0.3.0'),
    description=str('Instagram client for Django.'),
    long_description=README,
    author=str('Marco Pompili'),
    author_email=str('django@emarcs.org'),
    license=str('BSD-3 License'),
    url=str('https://github.com/marcopompili/django-instagram'),
    packages=find_packages(),
    plarforms='any',
    include_package_data=True,
    install_requires=[
        'django>=1.6',
        'lxml',
        'requests',
        'sorl-thumbnail',
        'Pillow',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 2.0',
    ],
)
