def number_of_differences(n, m, A, B):
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


assert number_of_differences(2, 3, [[1, 2, 3], [4, 5, 6]], [[1, 2, 4], [3, 5, 6]]) == 2
assert number_of_differences(2, 2, [[1, 2], [3, 4]], [[1, 2], [3, 4]]) == 0


def generate_sentences(subjects, predicates, objects):
    new_str_s = [""]
    for i in range(len(subjects)):
        for j in range(len(predicates)):
            for k in range(len(objects)):
                new_str_s.append(f"{subjects[i]} {predicates[j]} {objects[k]}.")

    new_str_s.sort()
    sorted_str = " ".join(new_str_s)
    print(sorted_str)
    return sorted_str


assert generate_sentences(["John", "Mary"], ["hates", "loves"],
                          ["apples", "bananas"]) == "John hates apples. John hates bananas. " \
                                                    "John loves apples. John loves bananas. " \
                                                    "Mary hates apples. Mary hates bananas. " \
                                                    "Mary loves apples. Mary loves bananas."

assert generate_sentences(["Vlad", "Hubie"], ["drives"],
                          ["car", "motorcycle", "bus"]) == "Hubie drives bus. " \
                                                       "Hubie drives car. " \
                                                       "Hubie drives motorcycle. " \
                                                       "Vlad drives bus. " \
                                                       "Vlad drives car. " \
                                                       "Vlad drives motorcycle."
