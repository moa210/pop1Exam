import math


def number_of_differences(n: object, m: object, A: object, B: object) -> object:
    diff = 0
    # j: int
    # i: int
    for i in range(n):
        for j in range(m):
            # print(A[i][j], B[i][j])
            if A[i][j] != B[i][j]:
                diff += 1
    print(diff)
    return diff


# my_set = {"one", "two", "tree"}
# print( my_set)
# # we discuss sets in detail later
#
# new_set = my_set.difference({"one", "two"})
# print(new_set)
#
# my_set.difference_update({"one", "two"})
# print(my_set)

assert number_of_differences(2, 3, [[1, 2, 3], [4, 5, 6]], [[1, 2, 4], [3, 5, 6]]) == 2
assert number_of_differences(2, 2, [[1, 2], [3, 4]], [[1, 2], [3, 4]]) == 0


class Airplane:
    def __init__(self, initX, initY, cons, init_fuel):
        self.fuel_level = init_fuel
        self.position = [initX, initY]
        self.consumption = cons

    def goto(self, X, Y):
        distance = math.sqrt(((X - self.position[0] ) ** 2) + (Y - self.position[1]) ** 2)
        fuel_needed = self.consumption * distance
        if fuel_needed < self.fuel_level:
            self.fuel_level -= fuel_needed
            self.position[0] = X
            self.position[1]= Y
            return True
        else:
            return False


def refuel(self, fuel):
    self.fuel += fuel


ap789 = Airplane(0, 0, 10, 3000)
assert ap789.goto(95, 70) == True
assert ap789.position[0] == 95 and ap789.position[1] == 70
# print(ap789.fuel_level - 1819.96)
assert abs(ap789.fuel_level - 1819.96) < 0.01


def longest_sequence(param):
    longest_so_far = 1
    letter = param[0]
    smallest_letter = param[0]
    current_sum = 1

    for i in range(1, len(param)):
        if param[i] == param[i - 1]:
            current_sum += 1
            if (longest_so_far <= current_sum) and (param[i] > letter):
                smallest_letter = param[i]
                letter = param[i]
            else:
                letter = param[i]
        else:
            current_sum = 1
        longest_so_far = max(longest_so_far, current_sum)

    print(smallest_letter, longest_so_far)
    return smallest_letter, longest_so_far


assert longest_sequence("dghhhmhmx") == ("h", 3)
assert longest_sequence("dhkkhhkkkt") == ("k", 3)
assert longest_sequence("abbbadddadd") == ("b", 3)
