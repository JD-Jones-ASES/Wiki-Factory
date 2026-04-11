"""Math Wiki problem generators.

Importing this package side-effects every submodule into the central
generator registry (see base.py).  The build pipeline (tools/build_problem_bank.py)
calls `from generators import all_generators` after importing this package.
"""
from . import geometry  # noqa: F401 (circles + pythagoras)
from . import algebra  # noqa: F401 (linear_equations, slope, quadratic_formula)
from . import pre_algebra  # noqa: F401 (percents)
from . import precalculus  # noqa: F401 (trig_core)
# Future branches are imported here as they come online:
# from . import trigonometry

from .base import all_generators, get_generator, Problem, Generator, Difficulty, DIFFICULTIES

__all__ = [
    "all_generators",
    "get_generator",
    "Problem",
    "Generator",
    "Difficulty",
    "DIFFICULTIES",
]
