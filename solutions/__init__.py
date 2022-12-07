from .util import *
from .day_01 import a as _01_a, b as _01_b, parse_input as _01_parse_input
from .day_02 import a as _02_a, b as _02_b, parse_input as _02_parse_input
from .day_03 import a as _03_a, b as _03_b, parse_input as _03_parse_input

days = {
    1: {"A": _01_a, "B": _01_b, "input": _01_parse_input},
    2: {"A": _02_a, "B": _02_b, "input": _02_parse_input},
    3: {"A": _03_a, "B": _03_b, "input": _03_parse_input},
}
