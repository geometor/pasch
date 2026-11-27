:order: 2
:layout: book

.. _pasch-sec-2-en:
.. _pasch-unit-2-en:

§ 2 & §§ 8–12: Planar Separation Axiom & Ideal Sheaves
======================================================

.. rubric:: Moritz Pasch — *Vorlesungen über neuere Geometrie* (1882), § 2 (pp. 17–27), §§ 8–11 (pp. 58–93) & § 12 (pp. 93–100)

.. contents:: In This Section
   :local:
   :depth: 2
   :backlinks: none

.. folio:: § 2
   :page: 17

§ 2. On the Plane and Pasch's Planar Separation Axiom (pp. 17–27)
-----------------------------------------------------------------

**Grundsatz I.** *Through any three points one can always lay a planar surface.*

**Grundsatz II.** *If two points of a straight segment belong to a planar surface (appropriately prolonged), then every interior point of the straight segment belongs to the planar surface.*

**Grundsatz III.** *If two planar surfaces share a common point, one can always specify at least a second point common to both.*

**Grundsatz IV (Pasch's Planar Separation Axiom, p. 21).** *Let* :math:`A, B, C` *be three points not lying in one straight line, and let* :math:`a` *be a straight line lying in the plane* :math:`ABC` *that passes through none of the points* :math:`A, B, C`: *if the straight line* :math:`a` *passes through a point inside the segment* :math:`AB`, *then it always passes also either through a point inside the segment* :math:`AC` *or through a point inside the segment* :math:`BC`.

.. picture:: /_static/figures/pasch_sec02_planar_axiom_euclid_gaps.svg
   :alt: Pasch's IV. Grundsatz (1882 p. 21) on triangle ABC and deductive proof of Euclid I.21 ray exit E on AC.
   :caption: **Pasch's IV. Grundsatz (1882 § 2, p. 21) & 10. Lehrsatz (p. 25):** Left: Any coplanar line :math:`\ell` entering :math:`\triangle ABC` along open segment :math:`AB` without meeting :math:`A, B, C` must exit through open segment :math:`AC` or :math:`BC` (never both). Right: Applying *Grundsatz IV* to sub-triangle :math:`\triangle AMC` proves Euclid ``I.21``'s interior ray exit :math:`E \in AC`.

**10. Lehrsatz (Exclusivity — A Line Cannot Cut All Three Open Sides, p. 25).** *In the configuration of Grundsatz IV, the straight line* :math:`a` *cannot pass simultaneously through a point inside* :math:`AB`, *a point inside* :math:`BC`, *and a point inside* :math:`AC`.

*Proof.* Suppose for contradiction that :math:`a` met open segments :math:`AB`, :math:`BC`, and :math:`AC` in interior points :math:`D, E, F` respectively. Being three distinct collinear points on :math:`a`, one of them—say :math:`F`—must by § 1 lie inside the segment :math:`DE` bounded by the other two (:math:`D\text{--}F\text{--}E`). Now consider triangle :math:`\triangle BDE` and the straight line :math:`g = [AC]`:

* Line :math:`g` passes through none of the vertices :math:`B, D, E` (since :math:`D` is interior to :math:`AB` and :math:`E` is interior to :math:`BC`).
* Line :math:`g` passes through :math:`F`, which lies **inside** side :math:`DE` of :math:`\triangle BDE`.
* Therefore, by **Grundsatz IV** applied to :math:`\triangle BDE`, line :math:`g = [AC]` would have to meet either segment :math:`BD` internally (impossible, since :math:`[AC] \cap [AB] = A` lies *outside* :math:`BD` by § 1 Grundsatz III) or segment :math:`BE` internally (equally impossible, since :math:`[AC] \cap [BC] = C` lies *outside* :math:`BE`)!

Hence a line avoiding :math:`A, B, C` that enters one open side of :math:`\triangle ABC` exits through **one and only one** of the other two open sides, and every straight line :math:`a` in a plane :math:`\alpha` partitions :math:`\alpha \setminus a` into **two** disjoint convex half-planes (*Halbebenen*): :math:`P, Q \notin a` lie on the *same side* of :math:`a` iff segment :math:`PQ` misses :math:`a`, and on *opposite sides* iff :math:`a` meets segment :math:`PQ` internally. :math:`\blacksquare`

.. folio:: §§ 8–11
   :page: 58

§§ 8–11. Ideal Sheaves Without Infinity & Harmonic Figures (pp. 58–93)
----------------------------------------------------------------------

**§ 8. Sheaves of Lines and Ideal Points (*Strahlenbündel und uneigentliche Punkte*).** In :person:`von Staudt <staudt>`'s *Geometrie der Lage* (§ 2), infinitely distant points were introduced by invoking Euclidean parallel directions—thereby relying on Euclid's Parallel Postulate and speaking figuratively of points "at infinity." Yet in actual observation we operate only within a **bounded spatial region**, where two coplanar lines :math:`g, h` may fail to intersect inside our region whether they are Euclidean parallels or merely converge far outside our region!

We therefore replace "points at infinity" by a rigorous finite construction:

1. Two coplanar lines :math:`g, h` together with any external point :math:`S` outside their plane determine two planes :math:`(S, g)` and :math:`(S, h)` intersecting along a unique ray :math:`k` through :math:`S`. The totality of all such lines :math:`k` determined across space forms a **sheaf of rays** (*Strahlenbündel*).
2. If :math:`g` and :math:`h` meet in an ordinary point :math:`P`, the sheaf consists simply of all lines through :math:`P` (*eigentliches Bündel*). If :math:`g` and :math:`h` do not meet, the sheaf is still completely determined by finite plane intersections (*uneigentliches Bündel*)—without ever assuming whether parallels are unique!
3. Calling **every** sheaf of rays a *projective point* (*Punkt im weiteren Sinne*), every planar flat pencil a *projective line*, and every planar sheaf a *projective plane*, all incidence axioms of three-dimensional projective geometry hold **unconditionally and without appeal to infinity**.

**§§ 10–11. Complete Quadrangle & Harmonic Separation Grounded on Order.** Armed with ideal sheaves (§§ 8–9) and planar separation (§ 2), :person:`von Staudt <staudt>`'s :term:`complete quadrangle <vollstaendiges-viereck>` construction (§ 6) now rests on complete logical foundations: using *Grundsatz IV* repeatedly across the four sub-triangles of quadrangle :math:`EFGH`, one proves **purely deductively** (without glancing at a figure!) that the harmonic conjugates :math:`(A, B)` and :math:`(C, D)` invariably :term:`separate one another <getrennte-paare>` on the projective line.

.. folio:: § 12
   :page: 93

§ 12. The Hypothetico-Deductive Manifesto (pp. 93–100)
------------------------------------------------------

Looking back over the edifice erected from §§ 1–11, we recognize the strict logical law that governs every genuinely deductive mathematical science (*p. 98*):

.. pull-quote::

   *"Indeed, if geometry is to be genuinely deductive, the process of inference must everywhere be independent of the meaning of the geometrical concepts, just as it must be independent of the diagrams; only the relations among the geometrical concepts laid down in the propositions and definitions employed may be taken into account. During the deduction it is certainly permissible and useful, though in no way necessary, to think of the meaning of the geometrical concepts appearing therein; in fact, precisely when this becomes necessary does a gap become manifest in the deduction and, when the gap cannot be eliminated by modifying the reasoning, the insufficiency of the propositions invoked as tools of proof."*

Whenever a classical proof appears to succeed only when we picture what "straight segment" or "interior" looks like in a drawing, an **unstated axiom** is hiding in our visual intuition. Once all :term:`nuclear propositions <stammsaetze>` (*Stammsätze*) are explicitly recorded at the threshold of the science:

* Every mathematical proof reduces to purely formal logical transformation of the stated relational hypotheses; and
* Every valid theorem admits an immediate **dual or structural reinterpretation** (such as projective :term:`reciprocity <reciprocitaet>` between points and planes, or algebraic coordinate models) simply by substituting any new system of objects that satisfies the exact same formal relations!
