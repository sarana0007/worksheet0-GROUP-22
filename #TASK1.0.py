#TASK1
def sum_nested_list(nested_list):
    """Calculate the sum of all numbers in a nested list.
    This function takes a list that may contain integers and other nested lists.
    It recursively traverses the list and sums all the integers, no matter how deeply nested they are.
    Args:
    nested_list (list) : A list that may contain integers or other lists of integers.
    Returns:
    int: The total sum of all integers in the nested list, including those in sublists.

    Example:
    >>> sum_nested_list([1, [2, [3, 4], 5], 6, [7, 8]])
    36
    >>> sum_nested_list([1, [2, 3], [4, [5]]])
    15
    """
    total = 0
    for element in nested_list:
        if isinstance(element, list): #check if the element is a list
            total += sum_nested_list(element) #recursively sum the nested list
        else:
            total += element #add the number to the total
    return total

#run the fuction
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
result = sum_nested_list(nested_list)
print("the total sum is : ", result)

#TASK2

def generate_permutations(s):
    """
    Generate all unique permutations of a given string.
    This function uses the concept of recursion to generate the permutations by fixing a character and permutatin the remaining characters. The characters are the listed in a set in oredr to ensure their uniqueness.

    Args:
    s (str) : The input string for which permutations are to be generated.

    Returns:
    list: A list of unique permutations of the input string.

    Examples:
    >>> generate_permutations("abc")
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    >>> generate_permutations("aab")
    ['aab', 'aba', 'baa']

    """
    #if the string has one character or is empty, return it as a single element list
    if len(s) <= 1:
        return[s]
    
    permutations = []

    for i, char in enumerate(s):
        #exclude the current character and permutate the remaining strings
        remaining = s[:i]+s[i+1:]
        for perm in generate_permutations(remaining):
            permutations.append(remaining)

    return list(set(permutations)) #remove the dupicates by converting to a set and back to a list

#test the function
print(generate_permutations("abc"))
print(generate_permutations("aab"))

#TASK3

def calculate_directory_size(directory):
    """
    Recursively calcualtes the total size of a drectory.

    Args:
    directory(dict) : A directry reperesenting a dircetory structure.

    Returns:
    int : The total size of the directory in KB.
    """

    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict):
            total_size += calculate_directory_size(value)
        else:
            total_size += value
    return total_size

#Sample directory structure
directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
        "file6.txt": 150
    }
}

#testing the function
total_size = calculate_directory_size(directory_structure)
print(f"Total size of the directory : {total_size} KB")