"""Comprehensive exact symbolic test suite for ``geometor.pasch``."""

from __future__ import annotations

from pathlib import Path

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.pasch import (
    PaschAuditResult,
    __version__,
    assert_straightedge_only,
    build_all_figures,
    demonstrate_euclid_i16_pasch_gap,
    demonstrate_euclid_i21_pasch_gap,
    demonstrate_pasch_axiom,
    get_repo_root,
    is_between,
    is_collinear,
    pair_separates,
    run,
)

Point = spg.Point


def test_version_and_cli() -> None:
    """Verify version and CLI execution."""
    assert __version__ == "0.1.0"
    assert run([]) == 0


def test_collinear_between_and_separation() -> None:
    """Verify collinearity, betweenness, and pair separation."""
    A = Point(0, 0)
    C = Point(1, 1)
    B = Point(3, 3)
    D = Point(sp.Rational(3, 2), sp.Rational(3, 2))
    E = Point(0, 2)

    assert is_collinear(A, C, B)
    assert not is_collinear(A, B, E)

    assert is_between(A, B, C)
    assert is_between(B, A, C)
    assert not is_between(A, B, A)
    assert not is_between(A, C, B)
    assert not is_between(A, B, E)

    F = Point(-3, -3)
    assert pair_separates(A, B, D, F)
    assert pair_separates(B, A, F, D)
    assert not pair_separates(A, D, B, F)
    assert not pair_separates(A, A, D, F)
    assert not pair_separates(A, B, D, E)


def test_straightedge_guard() -> None:
    """Verify straightedge assertion passes for lines and catches circles."""
    model = Model("straightedge_test", auto_intersect=False)
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    model.construct_line(A, B)
    assert_straightedge_only(model)

    model.construct_circle(A, B)
    with pytest.raises(Exception, match="Straightedge-only"):
        assert_straightedge_only(model)


def test_pasch_axiom_all_configurations() -> None:
    """Test Pasch's Planar Separation Axiom in all transversal configurations."""
    A = Point(0, 0)
    B = Point(6, 0)
    C = Point(2, 5)

    m1 = Model("pasch_ab_bc", auto_intersect=False)
    r1 = demonstrate_pasch_axiom(m1, A, B, C, Point(3, -1), Point(5, 3))
    assert isinstance(r1, PaschAuditResult)
    assert r1.satisfies_pasch
    assert {name for name, _ in r1.entered_sides} == {"AB", "BC"}
    assert_straightedge_only(m1)

    m2 = Model("pasch_ab_ac", auto_intersect=False)
    r2 = demonstrate_pasch_axiom(m2, A, B, C, Point(2, -1), Point(0, 3))
    assert r2.satisfies_pasch
    assert {name for name, _ in r2.entered_sides} == {"AB", "CA"}

    m3 = Model("pasch_ac_bc", auto_intersect=False)
    r3 = demonstrate_pasch_axiom(m3, A, B, C, Point(-1, 2), Point(6, 2))
    assert r3.satisfies_pasch
    assert {name for name, _ in r3.entered_sides} == {"BC", "CA"}

    m4 = Model("pasch_exterior", auto_intersect=False)
    r4 = demonstrate_pasch_axiom(m4, A, B, C, Point(0, -2), Point(6, -1))
    assert r4.satisfies_pasch
    assert r4.entered_sides == ()

    m5 = Model("pasch_vertex", auto_intersect=False)
    r5 = demonstrate_pasch_axiom(m5, A, B, C, C, Point(3, 0))
    assert r5.vertex_hits == ("C",)
    assert r5.satisfies_pasch


def test_euclid_i16_and_i21_pasch_audits() -> None:
    """Test resolution of Euclid's I.16 and I.21 diagrammatic betweenness gaps."""
    m_i16, i16 = demonstrate_euclid_i16_pasch_gap()
    assert_straightedge_only(m_i16)
    assert i16["B_C_D_between"] is True
    assert i16["A_E_C_between"] is True
    assert i16["B_E_F_between"] is True
    assert i16["K_between_A_and_D"] is True
    assert i16["pasch_audit_ABD"].satisfies_pasch is True

    m_i21, i21 = demonstrate_euclid_i21_pasch_gap()
    assert_straightedge_only(m_i21)
    assert i21["E_between_A_and_C"] is True
    assert i21["D_between_B_and_E"] is True
    assert i21["pasch_audit_AMC"].satisfies_pasch is True


def test_render_figures(tmp_path: Path) -> None:
    """Verify SVG figures render cleanly."""
    root = get_repo_root()
    assert (root / "pyproject.toml").exists()

    written = build_all_figures(tmp_path)
    assert len(written) == 4
    for svg_path in written:
        assert svg_path.exists()
        content = svg_path.read_text(encoding="utf-8")
        assert "<svg" in content
        assert "euclid-graphic" in content
