from __future__ import absolute_import

# import apis into api package
# from smoothnlp_api.api.investment_api import InvestmentApi
# from .news_api import NewsApi
# from .company_api import CompanyApi
# from smoothnlp_api.api.company_api import CompanyApi


import functools

def evaldata(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        data = func(*args, **kwargs)
        return eval(data)
    return inner

# import functools
# import time
#
# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()    # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()      # 2
#         run_time = end_time - start_time    # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return eval(value)
#     return wrapper_timer