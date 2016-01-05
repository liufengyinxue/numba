import math
from numba import types, utils
from numba.typing.templates import (AttributeTemplate, ConcreteTemplate,
                                    signature, Registry)

registry = Registry()
builtin_global = registry.register_global


@builtin_global(math.exp)
@builtin_global(math.fabs)
@builtin_global(math.sqrt)
@builtin_global(math.log)
@builtin_global(math.log1p)
@builtin_global(math.log10)
@builtin_global(math.sin)
@builtin_global(math.cos)
@builtin_global(math.tan)
@builtin_global(math.sinh)
@builtin_global(math.cosh)
@builtin_global(math.tanh)
@builtin_global(math.asin)
@builtin_global(math.acos)
@builtin_global(math.atan)
@builtin_global(math.asinh)
@builtin_global(math.acosh)
@builtin_global(math.atanh)
@builtin_global(math.degrees)
@builtin_global(math.radians)
class Math_unary(ConcreteTemplate):
    cases = [
        signature(types.float64, types.int64),
        signature(types.float64, types.uint64),
        signature(types.float32, types.float32),
        signature(types.float64, types.float64),
    ]

if utils.PYVERSION > (2, 6):
    for func in (math.erf, math.erfc, math.gamma, math.lgamma):
        Math_unary = builtin_global(func)(Math_unary)


@builtin_global(math.atan2)
class Math_atan2(ConcreteTemplate):
    cases = [
        signature(types.float64, types.int64, types.int64),
        signature(types.float64, types.uint64, types.uint64),
        signature(types.float32, types.float32, types.float32),
        signature(types.float64, types.float64, types.float64),
    ]

if utils.PYVERSION > (2, 6):
    @builtin_global(math.expm1)
    class Math_expm1(Math_unary):
        pass

@builtin_global(math.trunc)
class Math_converter(ConcreteTemplate):
    cases = [
        signature(types.intp, types.intp),
        signature(types.int64, types.int64),
        signature(types.uint64, types.uint64),
        signature(types.int64, types.float32),
        signature(types.int64, types.float64),
    ]

# math.floor and math.ceil return float on 2.x, int on 3.x
if utils.PYVERSION > (3, 0):
    @builtin_global(math.floor)
    @builtin_global(math.ceil)
    class Math_floor_ceil(Math_converter):
        pass
else:
    @builtin_global(math.floor)
    @builtin_global(math.ceil)
    class Math_floor_ceil(Math_unary):
        pass


@builtin_global(math.copysign)
class Math_copysign(ConcreteTemplate):
    cases = [
        signature(types.float32, types.float32, types.float32),
        signature(types.float64, types.float64, types.float64),
    ]


@builtin_global(math.hypot)
class Math_hypot(ConcreteTemplate):
    cases = [
        signature(types.float64, types.int64, types.int64),
        signature(types.float64, types.uint64, types.uint64),
        signature(types.float32, types.float32, types.float32),
        signature(types.float64, types.float64, types.float64),
    ]


@builtin_global(math.isinf)
@builtin_global(math.isnan)
class Math_predicate(ConcreteTemplate):
    cases = [
        signature(types.boolean, types.int64),
        signature(types.boolean, types.uint64),
        signature(types.boolean, types.float32),
        signature(types.boolean, types.float64),
    ]

if utils.PYVERSION >= (3, 2):
    @builtin_global(math.isfinite)
    class Math_isfinite(Math_predicate):
        pass


@builtin_global(math.pow)
class Math_pow(ConcreteTemplate):
    cases = [
        signature(types.float64, types.float64, types.int64),
        signature(types.float64, types.float64, types.uint64),
        signature(types.float32, types.float32, types.float32),
        signature(types.float64, types.float64, types.float64),
    ]

@builtin_global(math.frexp)
class Math_frexp(ConcreteTemplate):
    cases = [
        signature(types.Tuple((types.float64, types.intc)), types.float64),
        signature(types.Tuple((types.float32, types.intc)), types.float32),
    ]

@builtin_global(math.ldexp)
class Math_ldexp(ConcreteTemplate):
    cases = [
        signature(types.float64, types.float64, types.intc),
        signature(types.float32, types.float32, types.intc),
    ]
