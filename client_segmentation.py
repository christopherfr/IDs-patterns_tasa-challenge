import pandas as pd
import re

def main():
    df = pd.read_csv('data/segmentation.txt', header = None)

    # Search for type A clients
    a_pattern = r"(?:.*(?:A|E|I|O|U|a|e|i|o|u)+.*(.)\1+.*|.*(.)\2+.*(?:A|E|I|O|U|a|e|i|o|u)+.*|.*(A|E|I|O|U|a|e|i|o|u)\3+.*)"
    a_counter = 0
    a_indexes = []
    for index, row in df.iterrows():
        match = re.match(a_pattern, row[0])
        if match != None:
            a_counter += 1
            print(f'\rNumber of type A clients: {a_counter}', end='')
            a_indexes.append(index)
    print()
    df.drop(a_indexes, inplace=True) # Keep only the still unclassified clients
    del a_indexes # Free 2MB of memory :)

    # Search for type B clients
    b_pattern = r".*(?:1|3|5|7|9).*"
    b_counter = 0
    b_indexes = []
    for index, row in df.iterrows():
        upper_counter = 0
        lower_counter = 0
        match = re.match(b_pattern, row[0])
        for char in row[0]:
            if char.isupper():
                upper_counter += 1
            elif char.islower():
                lower_counter += 1
        if (upper_counter > lower_counter) or (match != None):
            b_counter += 1
            print(f'\rNumber of type B clients: {b_counter}', end='')
            b_indexes.append(index)
    print()
    df.drop(b_indexes, inplace=True) # Keep only the still unclassified clients
    del b_indexes

    # Search for type C clients
    c_pattern = r".*(?:jn|cg|ar|mp|fs|ic).*"
    c_counter = 0
    c_indexes = []
    for index, row in df.iterrows():
        match = re.match(c_pattern, row[0])
        if match != None:
            c_counter += 1
            print(f'\rNumber of type C clients: {c_counter}', end='')
            c_indexes.append(index)
    print()
    df.drop(c_indexes, inplace=True) # Keep only the still unclassified clients
    del c_indexes

    # Compute number of type D clients
    d_counter = df.size
    print(f'Number of type D clients: {d_counter}')

if __name__ == '__main__':
    main()