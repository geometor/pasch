=====
pasch
=====

the German geometer whose 1882 Vorlesungen established the axioms of linear order, planar separation, and modern hypothetico-deductive rigor

Edition Overview
----------------

- **Treatise**: *Vorlesungen über neuere Geometrie*
- **Author**: Moritz Pasch
- **Primary Edition Track**: ``docsrc/vorlesungen_1882/`` (``:layout: book``)
- **Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
Installation & Verification
---------------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   uv run --no-sync pytest
   ruff check src tests demos
   publish build

Usage
-----

.. code-block:: bash

   pasch --help

Links
-----

- **Documentation**: https://geometor.github.io/pasch
- **Repository**: https://github.com/geometor/pasch
- **Issues**: https://github.com/geometor/pasch/issues

License
-------

Licensed under the MIT License. See ``LICENSE`` for details.
