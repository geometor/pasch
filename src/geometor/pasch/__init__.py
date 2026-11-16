"""Public package interface for ``geometor.pasch``."""

from __future__ import annotations

from .app import main, run
from .order import (
    PaschAuditResult,
    assert_straightedge_only,
    demonstrate_euclid_i16_pasch_gap,
    demonstrate_euclid_i21_pasch_gap,
    demonstrate_pasch_axiom,
    is_between,
    is_collinear,
    pair_separates,
)
from .render import build_all_figures, get_repo_root

__version__ = "0.1.0"

__all__ = [
    "PaschAuditResult",
    "__version__",
    "assert_straightedge_only",
    "build_all_figures",
    "demonstrate_euclid_i16_pasch_gap",
    "demonstrate_euclid_i21_pasch_gap",
    "demonstrate_pasch_axiom",
    "get_repo_root",
    "is_between",
    "is_collinear",
    "main",
    "pair_separates",
    "run",
]
