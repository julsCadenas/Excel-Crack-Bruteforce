from itertools import product

def generateCombinations(string, filename):
    charCases = [(char.lower(), char.upper()) for char in string]
    combinations = product(*charCases)

    with open(filename, 'w') as file:
        for combo in combinations:
            file.write(''.join(combo) + '\n')

inputString = "insert password"
filename = "insert text file name"

generateCombinations(inputString, filename)

print(f"{inputString} combinations are now in {filename}.")