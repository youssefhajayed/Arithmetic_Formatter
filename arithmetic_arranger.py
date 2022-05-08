def arithmetic_arranger(problems, arg=False):
    arranged_problems = ""

    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    def test_errors(problem_list):

        if problem_list[1] not in ['+', '-']:
            return "Error: Operator must be \'+\' or \'-\'."
        elif not (problem_list[0].isdigit()):
            return "Error: Numbers must only contain digits."
        elif not problem_list[2].isdigit():
            return "Error: Numbers must only contain digits."
        elif int(problem_list[0]) > 9999 or int(problem_list[2]) > 9999:
            return "Error: Numbers cannot be more than four digits."
        else:
            return ""

    def print_problem(problem_list):
        dashes = ""
        for i in range(0, max(len(problem_list[0]), len(problem_list[2])) + 2):
            dashes = dashes + "-"

        if (len(problem_list[0]) > len(problem_list[2])):
            for i in range(0, len(problem_list[0]) - len(problem_list[2])):
                problem_list[2] = " " + problem_list[2]
            problem_list[0] = "  " + problem_list[0]
            problem_list[2] = problem_list[1] + " " + problem_list[2]


        else:
            for i in range(0, len(problem_list[2]) - len(problem_list[0]) + 2):
                problem_list[0] = " " + problem_list[0]
            problem_list[2] = problem_list[1] + " " + problem_list[2]

        list_of_results = [problem_list[0], problem_list[2], dashes]

        return list_of_results

    i = 0
    first_number = []
    second_number = []
    dashes = []
    result = []
    for problem in problems:

        problem_list = problem.split()
        arranged_problems = test_errors(problem_list)
        if len(arranged_problems) > 0:
            return arranged_problems
        list_of_results = print_problem(problem_list)
        first_number.append(list_of_results[0])
        second_number.append(list_of_results[1])
        dashes.append(list_of_results[2])
        if arg == True:
            result.append(str(eval(problem)))
        i = i + 1

    j = 0

    for j in range(0, i - 1):
        arranged_problems = arranged_problems + first_number[j] + "    "
    arranged_problems = arranged_problems + first_number[j + 1]
    arranged_problems = arranged_problems + "\n"

    for j in range(0, i - 1):
        arranged_problems = arranged_problems + second_number[j] + "    "
    arranged_problems = arranged_problems + second_number[j + 1]
    arranged_problems = arranged_problems + "\n"

    for j in range(0, i - 1):
        arranged_problems = arranged_problems + dashes[j] + "    "
    arranged_problems = arranged_problems + dashes[j + 1]
    if arg:
        arranged_problems = arranged_problems + "\n"

    if arg:
        for j in range(0, i - 1):
            number_of_spaces = len(dashes[j]) - len(result[j])
            space = ""
            for s in range(0, number_of_spaces):
                space = space + " "
            arranged_problems = arranged_problems + space + result[j] + "    "

        print(len(dashes[j + 1]))
        print(len(result[j + 1]))
        space = ""
        number_of_spaces = len(dashes[j + 1]) - len(result[j + 1])
        for s in range(0, number_of_spaces):
            space = space + " "
        arranged_problems = arranged_problems + space + result[j + 1]

    return arranged_problems
