"""
Labour work #2. Levenshtein distance.
""" 

def generate_edit_matrix(num_rows, num_cols):
    zero_matrix = []
    if isinstance(num_rows, int) and isinstance(num_cols, int)\
        and num_cols > 0 and num_rows > 0:
        for el in range(num_rows):
            string = []
            for el in range(num_cols):
                string.append(0)
            zero_matrix.append(string)
        return zero_matrix
    else:
        return zero_matrix

def initialize_edit_matrix(edit_matrix, add_weight, remove_weight):
    edit_matrix = list(edit_matrix)
    if edit_matrix != [] and edit_matrix[0] != []\
       and isinstance(add_weight, int) and isinstance(remove_weight, int):
        edit_matrix[0][0] = 0
        for i in range(1, len(edit_matrix)):
            edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
        for j in range(1, len(edit_matrix[0])):
            edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight
        return edit_matrix
    else:
        return edit_matrix

def minimum_value(numbers):
    if isinstance(numbers, tuple):
        res = min(list(numbers))
        return res
    else:
        return 0

def fill_edit_matrix(edit_matrix, add_weight, remove_weight, substitute_weight, original_word, target_word):
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int)\
            or not isinstance(original_word, str) or not isinstance(target_word, str):
        return list(edit_matrix)
    l_matrix = list(edit_matrix)
    for i, el in enumerate(l_matrix):
        if i == 0:
            continue
        for j, z in enumerate(el):
            if j == 0:
                continue
            removing = l_matrix[i - 1][j] + remove_weight
            adding = l_matrix[i][j - 1] + add_weight
            if original_word[i - 1] == target_word[j - 1]:
                substitution = l_matrix[i - 1][j - 1] + 0
            else:
                substitution = l_matrix[i - 1][j - 1] + substitute_weight
            numbers = tuple([removing, adding, substitution])
            el[j] = minimum_value(numbers)
    return l_matrix

def find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight):
    if isinstance(original_word, str) and isinstance(target_word, str)\
            and isinstance(add_weight, int) and isinstance(remove_weight, int) and isinstance(substitute_weight, int):
        matrix = tuple(generate_edit_matrix(len(original_word) + 1, len(target_word) + 1))
        matrix = initialize_edit_matrix(matrix, add_weight, remove_weight)
        filled_matrix = fill_edit_matrix(matrix, add_weight, remove_weight, substitute_weight, original_word, target_word)
        result = filled_matrix[-1][-1]
        return result
    else:
        return -1

def read_from_file(text_file):
    file = open(text_file, 'r')
    matrix = []
    for line in file:
        row = []
        for el in line:
            if el.isdigit():
                el = int(el)
                row.append(el)
        matrix.append(row)
    return matrix

def write_to_file(edit_matrix, text_file):
    file = open(text_file, 'w')
    for line in edit_matrix:
        row = ''
        for el in line:
            row += str(el) + ','
        file.write(row + '\n')
    file.close()

