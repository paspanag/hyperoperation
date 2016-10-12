def successor_function(a):
    return a+1

def curry_bimodal(function_to_curry, argument):
    return lambda x: function_to_curry(argument,x)

def recursive_builder(function_to_next):
    def recursive_function(initial, repititions, accumulating_variable=0):
        if repititions == accumulating_variable:
            return initial
        else:
            return recursive_function(function_to_next(initial), repititions, successor_function(accumulating_variable))
    return recursive_function

def higher_order(function_to_upgrade, initial_condition):
    return lambda x,y: recursive_builder(curry_bimodal(function_to_upgrade,x))(initial_condition, y)

add = recursive_builder(successor_function)
multiply = higher_order(add, 0)
exponential = higher_order(multiply, 1)
tetration = higher_order(exponential, 1)

assert 5 + 10 == add(5,10)
assert 2 + 0 == add(2,0)
assert 0 + 3 == add(0,3)
assert 25 + 11 == add(25,11)
assert 5 * 4 == multiply(5,4)
assert 100 * 4 == multiply(100,4)
assert 3 * 3 == multiply(3,3)
assert 2 * 0 == multiply(2,0)
assert 0 * 3 == multiply(0,3)
assert 2 * 1 == multiply(2,1)
assert 1 * 3 == multiply(1,3)
assert 5 ** 4 == exponential(5,4)
assert 3 ** 4 == exponential(3,4)
assert 3 ** 3 == exponential(3,3)
assert 2 ** 0 == exponential(2,0)
assert 0 ** 3 == exponential(0,3)
assert 2 ** 1 == exponential(2,1)
assert 1 ** 3 == exponential(1,3)
assert 2 ** 2 ** 2 == tetration(2,3)
