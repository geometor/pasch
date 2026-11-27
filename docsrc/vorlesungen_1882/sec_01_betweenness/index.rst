:order: 1
:layout: book

.. _pasch-sec-1-en:
.. _pasch-unit-1-en:

§ 1: Grounding Geometry & Linear Betweenness
============================================

.. rubric:: Moritz Pasch — *Vorlesungen über neuere Geometrie* (1882), *Vorwort*, *Einleitung* & § 1 (pp. 1–17)

.. contents:: In This Section
   :local:
   :depth: 2
   :backlinks: none

.. folio:: Vorwort & Einleitung
   :page: 1

Preface & Introduction (*Vorwort & Einleitung*, Giessen, 1882)
--------------------------------------------------------------

Modern projective geometry—elevated by :person:`Karl Georg Christian von Staudt <staudt>` into an autonomous science independent of measurement—still leaves unexamined a multitude of elementary assumptions concerning the relative order of points on a straight line and the separation of regions in a plane. Even in :person:`Euclid <euclid>`'s :cite:`*Elements* <euclid:elements>`, proofs continually rely upon facts read tacitly off a drawn figure rather than deduced from explicitly stated principles.

To place geometry upon an unassailable deductive foundation, we must separate two tasks strictly:

1. First, isolate the irreducible :term:`primitive concepts <stammbegriffe>` (*Stammbegriffe*: **point**, **straight segment** *gerade Strecke*, **planar surface** *ebene Fläche*, and later congruence) and state **every** empirical observation required of them in a closed list of :term:`nuclear propositions <stammsaetze>` (*Grundsätze* or *Stammsätze*).
2. Second, derive every subsequent concept (such as the full straight line, the ray, the entire plane, and ideal projective sheaves) and every theorem (*Lehrsatz*) by pure logical inference alone, without ever consulting sensible intuition or figures again.

Notice that in immediate physical observation we never encounter an infinite straight line, but only a bounded **straight segment** joining two endpoints :math:`A` and :math:`B`, together with **points lying interior to the segment** (*Punkte innerhalb der Strecke*, i.e., points lying :term:`between <zwischen>` :math:`A` and :math:`B`).

.. folio:: § 1
   :page: 4

§ 1. On the Straight Line (*Von der geraden Linie*, pp. 4–17)
-------------------------------------------------------------

**Grundsatz I.** *Between two distinct points one can always draw a straight segment, and indeed only one.*

We denote the straight segment joining :math:`A` and :math:`B` by :math:`AB` or :math:`BA`; :math:`A` and :math:`B` are its *endpoints* (*Endpunkte*). A statement ":math:`C` lies within segment :math:`AB`" means that :math:`C` lies **between** (:term:`zwischen <zwischen>`) :math:`A` and :math:`B`.

**Grundsatz II.** *One can always specify a point that lies inside a given straight segment.*

**Grundsatz III.** *If the point* :math:`C` *lies inside the segment* :math:`AB`, *then the point* :math:`A` *lies outside the segment* :math:`BC`.

**Grundsatz IV.** *If the point* :math:`C` *lies inside the segment* :math:`AB`, *then all points of the segment* :math:`AC` *belong also to the segment* :math:`AB`.

**Grundsatz V.** *If the point* :math:`C` *lies inside the segment* :math:`AB`, *then a point belonging to neither segment* :math:`AC` *nor segment* :math:`BC` *cannot belong to segment* :math:`AB` (*save* :math:`C` *itself*).

(*From Grundsätze I–V follow immediately the partition and transitivity laws of open interior segments: if* :math:`C` *lies between* :math:`A` *and* :math:`B`, *and* :math:`D` *lies between* :math:`A` *and* :math:`C`, *then* :math:`D` *lies between* :math:`A` *and* :math:`B` *while* :math:`C` *lies between* :math:`D` *and* :math:`B`.)

**Grundsatz VI (Segment Prolongation).** *If* :math:`A` *and* :math:`B` *are arbitrary distinct points, one can always choose a point* :math:`C` *in such a way that* :math:`B` *lies inside the segment* :math:`AC`.

**Grundsatz VII (Uniqueness of Prolongation).** *If the point* :math:`B` *lies inside both the segment* :math:`AC` *and the segment* :math:`AD`, *then either* :math:`C` *coincides with* :math:`D`, *or* :math:`C` *lies inside* :math:`BD`, *or* :math:`D` *lies inside* :math:`BC`.

**Grundsatz VIII (Disjointness of Distinct Lines).** *If* :math:`B` *lies inside* :math:`AC` *and* :math:`A` *lies inside* :math:`B'C`, *while* :math:`B` *and* :math:`B'` *do not belong to the same straight line with* :math:`A`, *no contradiction arises; on a single straight line, two distinct straight lines cannot share two distinct points*.

.. picture:: /_static/figures/pasch_sec01_linear_betweenness_separation.svg
   :alt: Moritz Pasch's linear betweenness axioms (Grundsätze I-VIII) for open segments AB and four-point separation of collinear pairs.
   :caption: **Pasch's Nuclear Axioms of Linear Betweenness (1882 § 1, pp. 4–16):** Bounded segments :math:`AB`, interior density (:math:`C` between :math:`A` and :math:`B`), prolongation (:math:`B` between :math:`A` and :math:`D`), and linear partition of four collinear points into a unique ordered quadruple :math:`A\text{--}C\text{--}B\text{--}D`.

**Definition of the Full Straight Line (*Gerade*).** Given two distinct points :math:`A` and :math:`B`, the **straight line** :math:`[AB]` consists of:

1. the endpoints :math:`A` and :math:`B`,
2. all points :math:`X` lying *inside* segment :math:`AB` (:math:`A\text{--}X\text{--}B`),
3. all points :math:`Y` such that :math:`B` lies inside :math:`AY` (:math:`A\text{--}B\text{--}Y`), and
4. all points :math:`Z` such that :math:`A` lies inside :math:`ZB` (:math:`Z\text{--}A\text{--}B`).

**Lehrsätze 1–23 (Selected Deductive Consequences on the Line).**

* **Lehrsatz 4.** Every straight line :math:`[AB]` is uniquely determined by **any two** distinct points lying upon it.
* **Lehrsatz 12 (Ray Separation by a Single Point).** Any point :math:`O` on a straight line :math:`g` divides all remaining points of :math:`g` into **two** non-empty classes (*Halbstrahlen* or opposite rays): two points :math:`P, Q \neq O` lie on the *same side* of :math:`O` when :math:`O` does **not** lie inside :math:`PQ`, and on *opposite sides* of :math:`O` when :math:`O` **does** lie inside :math:`PQ`.
* **Lehrsatz 19 (Four-Point Linear Order Theorem).** Given any **four** distinct collinear points, they can always be lettered in a unique way (up to reversal) as :math:`A, B, C, D` such that :math:`B` lies both between :math:`A, C` and between :math:`A, D`, while :math:`C` lies both between :math:`A, D` and between :math:`B, D`.
