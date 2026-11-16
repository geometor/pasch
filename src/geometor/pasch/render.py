"""Exact SymPy-driven SVG figure builder generating the standalone ``.euclid-graphic``
diagrams for ``geometor/pasch``.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, intersect_2d

from geometor.pasch.order import demonstrate_euclid_i21_pasch_gap, demonstrate_pasch_axiom

__all__ = ["build_all_figures"]


def get_repo_root() -> Path:
    """Return the absolute Path to the root of the ``geometor/pasch`` repository."""
    return Path(__file__).resolve().parents[3]


@dataclass
class _SvgCanvas:
    """Lightweight theme-adaptive ``.euclid-graphic`` SVG composer."""

    width: int
    height: int
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    title: str
    desc: str

    def __post_init__(self) -> None:
        self.elements: list[str] = []
        pad = 44.0
        sx = (self.width - 2 * pad) / (self.x_max - self.x_min)
        sy = (self.height - 2 * pad) / (self.y_max - self.y_min)
        self.scale = min(sx, sy)
        used_w = (self.x_max - self.x_min) * self.scale
        used_h = (self.y_max - self.y_min) * self.scale
        self.ox = (self.width - used_w) / 2.0
        self.oy = (self.height - used_h) / 2.0

    def map_pt(self, pt: spg.Point | tuple[float | sp.Expr, float | sp.Expr]) -> tuple[float, float]:
        if isinstance(pt, spg.Point):
            px, py = float(pt.x.evalf()), float(pt.y.evalf())
        else:
            px = float(sp.sympify(pt[0]).evalf())
            py = float(sp.sympify(pt[1]).evalf())
        sx = self.ox + (px - self.x_min) * self.scale
        sy = self.height - (self.oy + (py - self.y_min) * self.scale)
        return sx, sy

    def seg(
        self,
        p1: spg.Point | tuple[float | sp.Expr, float | sp.Expr],
        p2: spg.Point | tuple[float | sp.Expr, float | sp.Expr],
        *,
        cls: str = "line-primary",
    ) -> None:
        x1, y1 = self.map_pt(p1)
        x2, y2 = self.map_pt(p2)
        self.elements.append(
            f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" class="{cls}" />'
        )

    def poly(
        self,
        pts: list[spg.Point | tuple[float | sp.Expr, float | sp.Expr]],
        *,
        cls: str = "poly-fill",
    ) -> None:
        coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in (self.map_pt(p) for p in pts))
        self.elements.append(f'  <polygon points="{coords}" class="{cls}" />')

    def dot(
        self,
        pt: spg.Point | tuple[float | sp.Expr, float | sp.Expr],
        label: str,
        *,
        dx: int = 8,
        dy: int = -8,
        cls: str = "pt-given",
        r: float = 4.2,
        anchor: str = "start",
    ) -> None:
        cx, cy = self.map_pt(pt)
        self.elements.append(f'  <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.1f}" class="{cls}" />')
        lx = cx + dx
        ly = cy + dy
        esc_label = escape(label)
        self.elements.append(
            f'  <text x="{lx:.2f}" y="{ly:.2f}" class="lbl-pt" text-anchor="{anchor}">{esc_label}</text>'
        )

    def caption(self, x: float, y: float, text: str) -> None:
        self.elements.append(
            f'  <text x="{x:.1f}" y="{y:.1f}" class="lbl-caption" text-anchor="middle">{escape(text)}</text>'
        )

    def render(self) -> str:
        body = "\n".join(self.elements)
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" class="euclid-graphic" role="img" aria-label="{escape(self.title)}">
<title>{escape(self.title)}</title>
<desc>{escape(self.desc)}</desc>
<style>
  .euclid-graphic {{
    display: block;
    max-width: 100%;
    height: auto;
    margin: 1.5rem auto;
    background: var(--color-surface, #ffffff);
    border: 1px solid var(--color-border-subtle, #e0e0e0);
    border-radius: 6px;
  }}
  .line-primary {{ stroke: var(--color-gold, #c8922a); stroke-width: 2.2px; stroke-linecap: round; }}
  .line-secondary {{ stroke: var(--color-indigo, #3b5998); stroke-width: 1.8px; stroke-linecap: round; }}
  .line-accent {{ stroke: var(--color-crimson, #b02a30); stroke-width: 1.8px; stroke-linecap: round; }}
  .line-guide {{ stroke: var(--color-text-muted, #8a8a8a); stroke-width: 1.1px; stroke-dasharray: 4 3; opacity: 0.85; }}
  .line-result {{ stroke: var(--color-emerald, #1f7a4d); stroke-width: 2.4px; stroke-linecap: round; }}
  .poly-fill {{ fill: var(--color-poly-fill, rgba(200, 146, 42, 0.08)); stroke: var(--color-gold, #c8922a); stroke-width: 1.6px; stroke-linejoin: round; }}
  .poly-accent {{ fill: var(--color-poly-fill-accent, rgba(59, 89, 152, 0.10)); stroke: var(--color-indigo, #3b5998); stroke-width: 1.5px; stroke-linejoin: round; }}
  .pt-given {{ fill: var(--color-indigo, #3b5998); stroke: var(--color-surface, #ffffff); stroke-width: 1.5px; }}
  .pt-aux {{ fill: var(--color-text-muted, #666666); stroke: var(--color-surface, #ffffff); stroke-width: 1.5px; }}
  .pt-result {{ fill: var(--color-crimson, #b02a30); stroke: var(--color-surface, #ffffff); stroke-width: 1.5px; }}
  .pt-emerald {{ fill: var(--color-emerald, #1f7a4d); stroke: var(--color-surface, #ffffff); stroke-width: 1.5px; }}
  .lbl-pt {{ font-family: "Cinzel", "STIX Two Text", "DejaVu Serif", serif; font-size: 13.5px; fill: var(--color-text-primary, #1a1a1a); font-style: italic; }}
  .lbl-caption {{ font-family: "Cinzel", "STIX Two Text", "DejaVu Serif", serif; font-size: 13.5px; fill: var(--color-text-primary, #2a2a2a); font-style: italic; }}
  @media (prefers-color-scheme: dark) {{
    .euclid-graphic {{
      background: var(--color-surface, #14161a);
      border-color: var(--color-border-subtle, #2b303a);
    }}
    .line-primary {{ stroke: #e0aa3e; }}
    .line-secondary {{ stroke: #6b8fd4; }}
    .line-accent {{ stroke: #e0535a; }}
    .line-guide {{ stroke: #7a8291; }}
    .line-result {{ stroke: #38b775; }}
    .poly-fill {{ fill: rgba(224, 170, 62, 0.12); stroke: #e0aa3e; }}
    .poly-accent {{ fill: rgba(107, 143, 212, 0.14); stroke: #6b8fd4; }}
    .pt-given {{ fill: #6b8fd4; stroke: #14161a; }}
    .pt-aux {{ fill: #9aa0a6; stroke: #14161a; }}
    .pt-result {{ fill: #e0535a; stroke: #14161a; }}
    .pt-emerald {{ fill: #38b775; stroke: #14161a; }}
    .lbl-pt {{ fill: #e6e8eb; }}
    .lbl-caption {{ fill: #e6e8eb; }}
  }}
</style>
{body}
</svg>
"""


def _fig_pasch_linear_betweenness_separation() -> str:
    """Pasch linear betweenness (§ 1) vs. 4-point projective pair separation (§ 11)."""
    S = spg.Point(0, 4)
    A = spg.Point(-4, 0)
    C = spg.Point(-1, 0)
    B = spg.Point(2, 0)
    D = spg.Point(5, 0)

    m_line = spg.Line(spg.Point(-4, 2), spg.Point(5, sp.Rational(7, 2)))
    Ap = intersect_2d(spg.Line(S, A), m_line)[0]
    Cp = intersect_2d(spg.Line(S, C), m_line)[0]
    Bp = intersect_2d(spg.Line(S, B), m_line)[0]
    Dp = intersect_2d(spg.Line(S, D), m_line)[0]

    cv = _SvgCanvas(
        width=760,
        height=400,
        x_min=-5.0,
        x_max=6.0,
        y_min=-0.9,
        y_max=4.7,
        title="Moritz Pasch (1882) §§ 1 & 11: Open Linear Betweenness vs. 4-Point Projective Separation",
        desc="Segment interior points C between A and B vs. exterior point D, showing pair separation AB // CD preserved across perspective section.",
    )
    m_left = intersect_2d(
        m_line, spg.Line(spg.Point(sp.Rational(-9, 2), -5), spg.Point(sp.Rational(-9, 2), 5))
    )[0]
    m_right = intersect_2d(
        m_line, spg.Line(spg.Point(sp.Rational(11, 2), -5), spg.Point(sp.Rational(11, 2), 5))
    )[0]
    cv.seg((-4.7, 0), (5.6, 0), cls="line-primary")
    cv.seg(A, B, cls="line-accent")
    cv.seg(m_left, m_right, cls="line-secondary")
    for p in (A, C, B, D):
        cv.seg(S, p, cls="line-guide")

    cv.dot(S, "S", dx=0, dy=-10, cls="pt-aux", anchor="middle")
    cv.dot(A, "A", dx=0, dy=19, anchor="middle")
    cv.dot(C, "C (inside AB)", dx=0, dy=19, cls="pt-result", anchor="middle")
    cv.dot(B, "B", dx=0, dy=19, anchor="middle")
    cv.dot(D, "D (outside AB)", dx=0, dy=19, cls="pt-emerald", anchor="middle")

    cv.dot(Ap, "A'", dx=-8, dy=-8, cls="pt-aux", anchor="end")
    cv.dot(Cp, "C'", dx=-4, dy=-10, cls="pt-result", anchor="middle")
    cv.dot(Bp, "B'", dx=6, dy=-10, cls="pt-aux")
    cv.dot(Dp, "D'", dx=8, dy=-8, cls="pt-emerald")
    cv.caption(
        380,
        382,
        "Pasch (1882) § 1 Grundsätze V–VIII & Lehrsätze 19–23: C lies between A and B while D lies outside AB, yielding invariant pair separation AB // CD",
    )
    return cv.render()


def _fig_pasch_planar_axiom_euclid_gaps() -> str:
    """Pasch's Grundsatz IV (§ 2 p. 21) & Crossbar Proof of Euclid I.21."""
    m_left = Model("fig_left", auto_intersect=False, enable_logging=False)
    A0 = m_left.given_point(-8, 0, label="A")
    B0 = m_left.given_point(-2, 0, label="B")
    C0 = m_left.given_point(-5, 5, label="C")
    P0 = m_left.given_point(-8, 1, label="P")
    Q0 = m_left.given_point(-1, 3, label="Q")
    audit = demonstrate_pasch_axiom(m_left, A0, B0, C0, P0, Q0)
    hit1 = audit.entered_sides[0][1]
    hit2 = audit.entered_sides[1][1]

    _, i21 = demonstrate_euclid_i21_pasch_gap()
    sh = sp.Integer(1)
    A1 = spg.Point(0 + sh, 0)
    B1 = spg.Point(8 + sh, 0)
    C1 = spg.Point(3 + sh, 6)
    D1 = spg.Point(3 + sh, 2)
    M1 = spg.Point(i21["M_on_AB"].x + sh, i21["M_on_AB"].y)
    E1 = spg.Point(i21["E_on_AC"].x + sh, i21["E_on_AC"].y)

    cv = _SvgCanvas(
        width=820,
        height=430,
        x_min=-8.8,
        x_max=9.8,
        y_min=-1.0,
        y_max=6.7,
        title="Moritz Pasch (1882) § 2 IV. Grundsatz (p. 21) & Resolution of Euclid I.21",
        desc="Left: Pasch's planar line-triangle separation axiom. Right: Deductive proof of Euclid I.21 ray exit E on AC by applying Pasch's Axiom to sub-triangle AMC.",
    )
    cv.poly([A0, B0, C0], cls="poly-fill")
    cv.seg(P0, Q0, cls="line-accent")
    cv.dot(A0, "A", dx=-8, dy=16, anchor="end")
    cv.dot(B0, "B", dx=8, dy=16)
    cv.dot(C0, "C", dx=0, dy=-10, anchor="middle")
    cv.dot(hit1, "X₁ (entry)", dx=-10, dy=-8, cls="pt-result", r=4.8, anchor="end")
    cv.dot(hit2, "X₂ (forced exit)", dx=10, dy=6, cls="pt-result", r=4.8)

    cv.poly([A1, B1, C1], cls="poly-fill")
    cv.poly([A1, M1, C1], cls="poly-accent")
    cv.seg(C1, M1, cls="line-secondary")
    cv.seg(
        B1,
        (
            float((E1.x - (B1.x - E1.x) * sp.Rational(1, 6)).evalf()),
            float((E1.y - (B1.y - E1.y) * sp.Rational(1, 6)).evalf()),
        ),
        cls="line-result",
    )
    cv.dot(A1, "A", dx=-8, dy=16, anchor="end")
    cv.dot(B1, "B", dx=8, dy=16)
    cv.dot(C1, "C", dx=0, dy=-10, anchor="middle")
    cv.dot(M1, "M", dx=0, dy=18, cls="pt-aux", anchor="middle")
    cv.dot(D1, "D", dx=9, dy=-4, cls="pt-result")
    cv.dot(E1, "E ∈ AC", dx=-10, dy=-6, cls="pt-emerald", r=5.0, anchor="end")

    cv.caption(205, 412, "(a) Pasch § 2 IV. Grundsatz: Entry X₁ forces exit X₂")
    cv.caption(605, 412, "(b) Euclid I.21: Pasch on △AMC forces ray BD to exit AC at E")
    return cv.render()


def build_all_figures(output_dir: Path | None = None) -> list[Path]:
    """Generate the standalone ``.euclid-graphic`` SVG figures in ``docsrc/_static/figures/``."""
    target_dir = output_dir or (get_repo_root() / "docsrc" / "_static" / "figures")
    target_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    fig1_svg = _fig_pasch_linear_betweenness_separation()
    fig2_svg = _fig_pasch_planar_axiom_euclid_gaps()

    # Write both canonical sec and backward-compatible pasch_unit filenames
    for fname, content in [
        ("pasch_unit1_linear_betweenness_separation.svg", fig1_svg),
        ("pasch_sec01_linear_betweenness_separation.svg", fig1_svg),
        ("pasch_unit2_planar_axiom_euclid_gaps.svg", fig2_svg),
        ("pasch_sec02_planar_axiom_euclid_gaps.svg", fig2_svg),
    ]:
        p = target_dir / fname
        p.write_text(content, encoding="utf-8")
        written.append(p)

    return written
