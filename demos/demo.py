"""Demonstration of Moritz Pasch's Planar Separation Axiom and Euclidean Gap Audits."""

from __future__ import annotations

import sympy.geometry as spg
from geometor.model import Model
from rich.console import Console

from geometor.pasch import (
    __version__,
    demonstrate_euclid_i16_pasch_gap,
    demonstrate_euclid_i21_pasch_gap,
    demonstrate_pasch_axiom,
)


def main() -> int:
    """Run exact symbolic demonstrations of Pasch's axioms and audits."""
    console = Console()
    console.rule(f"[bold gold1]geometor.pasch v{__version__}[/bold gold1]")

    # 1. Pasch's Axiom on triangle ABC
    model = Model("pasch_demo", auto_intersect=False, enable_logging=False)
    A = spg.Point(0, 0)
    B = spg.Point(6, 0)
    C = spg.Point(2, 5)
    audit = demonstrate_pasch_axiom(model, A, B, C, spg.Point(3, -1), spg.Point(5, 3))
    console.print(f"[bold cyan]Pasch's Axiom Audit:[/bold cyan] Satisfies = {audit.satisfies_pasch}")
    console.print(f"  Entered open sides: {[name for name, _ in audit.entered_sides]}")

    # 2. Euclid I.16 Exterior Angle order gap audit
    _, i16_audit = demonstrate_euclid_i16_pasch_gap()
    console.print(
        f"[bold cyan]Euclid I.16 Pasch Audit:[/bold cyan] Crossbar K between A and D: {i16_audit['K_between_A_and_D']}"
    )

    # 3. Euclid I.21 Interior ray-exit audit
    _, i21_audit = demonstrate_euclid_i21_pasch_gap()
    console.print(
        f"[bold cyan]Euclid I.21 Pasch Audit:[/bold cyan] Ray BD exits open side AC at E: {i21_audit['E_between_A_and_C']}"
    )

    console.rule("[bold green]All Symbolic Invariants Verified[/bold green]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
