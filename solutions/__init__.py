from .util import *
from .day_01 import a as _01_a, b as _01_b, parse_input as _01_parse_input
from .day_02 import a as _02_a, b as _02_b, parse_input as _02_parse_input
from .day_03 import a as _03_a, b as _03_b, parse_input as _03_parse_input
from .day_04 import a as _04_a, b as _04_b, parse_input as _04_parse_input
from .day_05 import a as _05_a, b as _05_b, parse_input as _05_parse_input
from .day_06 import a as _06_a, b as _06_b, parse_input as _06_parse_input
from .day_07 import a as _07_a, b as _07_b, parse_input as _07_parse_input

days = {
    1: {"A": _01_a, "B": _01_b, "input": _01_parse_input},
    2: {"A": _02_a, "B": _02_b, "input": _02_parse_input},
    3: {"A": _03_a, "B": _03_b, "input": _03_parse_input},
    4: {"A": _04_a, "B": _04_b, "input": _04_parse_input},
    5: {"A": _05_a, "B": _05_b, "input": _05_parse_input},
    6: {"A": _06_a, "B": _06_b, "input": _06_parse_input},
    7: {"A": _07_a, "B": _07_b, "input": _07_parse_input},
}
