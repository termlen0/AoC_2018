#!/usr/bin/envy python


def compute_frequency(data):
    '''Day1 Part 1'''
    freq = 0
    for element in data:
        if element[0] == '+':
            freq += int(element[1:])
        elif element[0] == '-':
            freq -= int(element[1:])
    return freq


def do_operation(freq, next_freq):
    if next_freq[0] == '+':
        freq += int(next_freq[1:])
    elif next_freq[0] == '-':
        freq -= int(next_freq[1:])
    return freq


def find_repeat(data):
    global seen_frequencies
    if len(seen_frequencies) == 0:
        seen_frequencies.append(0)
    for element in data:
        result = do_operation(seen_frequencies[-1], element)
        seen_frequencies.append(result)
        if seen_frequencies.count(result) > 1:
            return(result)
    result = find_repeat(data)
    return(result)


if __name__ == '__main__':
    with open('input1.1') as fh:
        data = fh.read()
        data = data.split('\n')
        # Remove trailing element
        data.pop(-1)
    # Day1 Part1
    print(compute_frequency(data))
    # Day1 Part2
    seen_frequencies = []
    print(find_repeat(data))
