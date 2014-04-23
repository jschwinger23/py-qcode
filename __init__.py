__version__ = (0, 0, 0)

import simulation as _sim
import error as _err
import lattice as _lat
import code as _cod
import decoder as _dec

__modules = [_sim, _err, _lat, _cod, _dec]
map(reload, __modules)

from simulation import *
from error import *
from lattice import *
from code import *
from decoder import *

__all__ = reduce(lambda a, b: a+b, map(lambda mod: mod.__all__,
                                     __modules)) + ['__version__']