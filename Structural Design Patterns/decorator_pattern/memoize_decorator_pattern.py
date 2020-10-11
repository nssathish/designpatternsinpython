def memoize(fn):
    cache = {}

    def memoized(n):
        if cache.get(n) is None:
            cache[n] = fn(n)
        return cache[n]

    return memoized

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    import timeit
    print(timeit.timeit("fib(100)", "from __main__ import fib"))