#!/usr/bin/env python

# Websnort - Web service for analysing pcap files with snort
# Copyright (C) 2013-2015 Steve Henderson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

def load_version():
    "Returns the current project version"
    from websnort import version
    return version.__version__

setup(
    name="websnort",
    version=load_version(),
    packages=['websnort', 'websnort.ids'],
    zip_safe=False,
    author="Steve Henderson",
    author_email="steve.henderson@hendotech.com.au",
    url="https://github.com/shendo/websnort",
    description="Web service for analysing pcap files with snort",
    long_description=open('README.rst').read(),
    entry_points={"console_scripts": ['websnort = websnort.web:main'],
                  "websnort.ids": ['snort = websnort.ids.snort:Snort',
                                   'suricata = websnort.ids.suricata:Suricata']
          },
    include_package_data=True,
    license="GPL",
    install_requires=open('requirements.txt').readlines(),
    tests_require=['pytest>=2.5'],
    setup_requires=['pytest-runner'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Security'
    ],
)
