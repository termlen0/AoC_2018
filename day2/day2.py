def checksum(data):
    three_letter = 0
    two_letter = 0
    for box_code in data:
        two_letter_flag = False
        three_letter_flag = False
        if len(box_code) != len(set(box_code)):
            for letter in box_code:
                if box_code.count(letter) == 2:
                    if not two_letter_flag:
                        two_letter += 1
                        two_letter_flag = True
                elif box_code.count(letter) == 3:
                    if not three_letter_flag:
                        three_letter += 1
                        three_letter_flag = True
    checksum = two_letter * three_letter
    return(checksum)


def identical(data):
    for word in data:
        for other in data:
            inequalities = 0
            for x, y in zip(word, other):
                if x != y:
                    inequalities += 1
            if inequalities == 1:
                common = set(word).difference(set(other))
                if common:
                    common = common.pop()
                    result = word.replace(common, '')
                else:
                    common = set(other).difference(set(word)).pop()
                    result = other.replace(common, '')
                return result


if __name__ == '__main__':
    with open('day2.input') as fh:
        data = fh.read().split('\n')
    # Cleanup the list
    data.pop()
    # Part 1
    print(checksum(data))
    # Part 2
    print(identical(data))
