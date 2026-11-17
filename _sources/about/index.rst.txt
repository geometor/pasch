:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:
.. _about-pasch:

=====
About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

The GEOMETOR edition of :person:`Moritz Pasch <pasch>` presents the foundational treatise that established modern mathematical axiomatics and resolved the hidden diagrammatic assumptions of Greek and projective geometry:

* **Moritz Pasch** (*Vorlesungen über neuere Geometrie*, :cite:`1882 <pasch:1882>`):
  Author of the 1882 Giessen lectures that supplied the missing topological foundations of classical deduction. By isolating the nuclear axioms of linear :term:`betweenness <zwischen>`, formulating Pasch's Planar Separation Axiom (:term:`IV. Grundsatz <pasch-grundsatz>`), and reconstructing projective ideal elements strictly from finite sheaves (*Bündel*) without appeal to infinity, Pasch formulated the modern hypothetico-deductive criterion directly inherited by :person:`David Hilbert <hilbert>`, :person:`Bertrand Russell <russell>`, :person:`Oswald Veblen <veblen>`, :person:`Fr. Petrus Hoenen <hoenen>`, and :person:`Alfred Tarski <tarski>`.

This critical edition extracts the implicit deductive architecture of Pasch's treatise into an addressable, machine-readable semantic corpus. Every proposition, definition, betweenness relation, and planar transversal step is indexed with stable anchors, linked to synchronized four-track codices (*English translation, original German print witness, conceptual summary, and scholarly notes*), and verified symbolically in ``geometor.pasch.order``.

The GEOMETOR Mission
--------------------

GEOMETOR is an ongoing research initiative founded by **phi ARCHITECT** dedicated to recovering, formalizing, and revitalizing foundational geometric and philosophical heritage through three pillars:

1. **Extracting Historical Semantic Knowledge**:
   Moving beyond passive scans to recover the living deductive structure of geometric treatises—elevating verbatim prose, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured semantic graphs.

2. **Exact Symbolic Grounding (``geometor.model``)**:
   Anchoring geometric constructions in 100% exact symbolic algebra (`SymPy <https://www.sympy.org/>`_) and Rational Trigonometry invariants over exact algebraic fields ($\mathbb{Q}$, $\mathbb{Q}(\phi)$). In ``geometor.pasch``, linear betweenness and triangle transversals are verified with exact orientation determinants and signed inner products, demonstrating that planar separation holds free from floating-point distortion.

3. **Repurposing Knowledge Across Mediums**:
   Re-deploying extracted semantic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (`photon-platform/publish <https://github.com/phiarchitect/publish>`_), computable deductive canons (``geometor.elements``, ``geometor.staudt``, ``geometor.hilbert``), interactive SVG laboratories, and visual broadcasts.

Sources, Provenance & Repository Architecture
---------------------------------------------

The texts and diagrams in this edition derive directly from high-resolution scans of the original 1882 German edition:

* **Pasch (1882):** *Vorlesungen über neuere Geometrie*. Leipzig: Verlag von B. G. Teubner, 1882 (iv + 202 pp.). Public-domain German witness archived in ``resources/vorlesungen_1882/sources/pasch_1882_vorlesungen_de.txt`` (SHA-256: ``02f734bf32ea772d77fcd7bafc64e738116e51e759a639c09116c6087b094b56``).
* **Python Package**: ``src/geometor/pasch/`` (Python 3.13)
* **Codex Edition Track**: ``docsrc/vorlesungen_1882/`` (``:layout: book``)
* **Edition Structure Map**: ``resources/vorlesungen_1882/structure_map.json``
* **Folio Map**: ``resources/vorlesungen_1882/folio_map.json``
* **Scholarly Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
* **Automated Verification**: ``tests/`` (``pytest``) and ``docsrc/`` (``publish build``)

For further exploration of this edition's structure:

* :ref:`Reader's Guide & Usage Instructions <usage>`
* :ref:`Systematic Bibliography <bibliography>`
* :ref:`People & Historical Figures <persons>`
* :ref:`Bilingual Mathematical Glossary <glossary>`
* :doc:`Exact Demonstrations <../demos/index>`
* :doc:`Python Symbolic API Reference <../modules/index>`
