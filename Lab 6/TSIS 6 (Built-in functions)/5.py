def all_elements_true(t):
    return all(t)
tuple1 = (True, True, True)
tuple2 = (False, True, True)
tuple3 = (True, False, True)
print(all_elements_true(tuple1))  # Output: True
print(all_elements_true(tuple2))  # Output: False
print(all_elements_true(tuple3))  # Output: False