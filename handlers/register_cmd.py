from handlers.cart import register_handlers_cart
from handlers.cmd import register_handlers_start
from handlers.math.math import register_handlers_math
from handlers.math.math_formulas import register_handlers_math_formulas
from handlers.math.math_taimer import register_handlers_math_timer
from handlers.math.mentally_math import register_handlers_math_mentally
from handlers.math.problems_category_math import register_handlers_math_problem_category


def reg_cmd(dp):
    register_handlers_start(dp)
    register_handlers_cart(dp)
    register_handlers_math(dp)
    register_handlers_math_mentally(dp)
    register_handlers_math_formulas(dp)
    register_handlers_math_problem_category(dp)
    register_handlers_math_timer(dp)

    # register_handlers_math_formulas_inline(dp)


def reg_call_cmd(dp):
    # register_handlers_math_formulas_inline(data_b)
    pass
