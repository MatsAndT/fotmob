========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/fotmob/badge/?style=flat
    :target: https://fotmob.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/MatsAndT/fotmob.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/MatsAndT/fotmob

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/MatsAndT/fotmob?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/MatsAndT/fotmob

.. |requires| image:: https://requires.io/github/MatsAndT/fotmob/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/MatsAndT/fotmob/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/MatsAndT/fotmob/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/MatsAndT/fotmob

.. |version| image:: https://img.shields.io/pypi/v/fotmob.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/fotmob

.. |wheel| image:: https://img.shields.io/pypi/wheel/fotmob.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/fotmob

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/fotmob.svg
    :alt: Supported versions
    :target: https://pypi.org/project/fotmob

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/fotmob.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/fotmob

.. |commits-since| image:: https://img.shields.io/github/commits-since/MatsAndT/fotmob/v0.0.3.svg
    :alt: Commits since latest release
    :target: https://github.com/MatsAndT/fotmob/compare/v0.0.3...master



.. end-badges

A Python wrapper around the unofficial FotMob API

* Free software: MIT license

Installation
============

::

    pip install fotmob

You can also install the in-development version with::

    pip install https://github.com/MatsAndT/fotmob/archive/master.zip


Documentation
=============


https://fotmob.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
