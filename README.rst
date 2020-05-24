Pelican FIX Engine
==================

.. image:: https://dev.azure.com/cloudwall/Pelican/_apis/build/status/cloudwall.pelican?branchName=master
    :target: https://dev.azure.com/cloudwall/Pelican/_build/latest?definitionId=9

.. image:: https://img.shields.io/pypi/v/pelican-fix.svg
    :target: https://pypi.org/project/pelican-fix/

.. image:: https://img.shields.io/pypi/l/pelican-fix.svg
    :target: https://pypi.org/project/pelican-fix/

.. image:: https://img.shields.io/pypi/pyversions/pelican-fix.svg
    :target: https://pypi.org/project/pelican-fix/

*A framework for building FIX clients and servers in Python*

About Pelican FIX
-----------------

Pelican FIX is a simple FIX engine with support for arbitrary protocols.

Installation
------------

Pelican runs on `Python <http://www.python.org/>`_ 3.7 or above. To install Pelican:

.. code:: console

    pip3 install pelican-fix

Credits
-------

Pelican's FIX engine is heavily based on `maxtwen's AIOPyFix <https://github.com/maxtwen/AIOPyFix>`_; the XML FIX
specification files come from the `QuickFIX <https://github.com/quickfix/quickfix/tree/master/spec>`_ project,
and the FIX message parsing uses `David Arnold's simplefix <https://github.com/da4089/simplefix>`_.