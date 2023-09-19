def read_boxes(instruments):
    """
    >>> boxes = read_boxes('boxes01.txt')
    >>> boxes
    {'guitar': 'conga', 'saxophone': 'banjo', 'conga': 'maracas', 'drum set': 'saxophone', 'trumpet': 'guitar', 'bass guitar': 'trombone', 'synthesizer': 'trumpet', 'banjo': 'drum set', 'trombone': 'bass guitar', 'maracas': 'synthesizer'}
    """
    answer = {}
    a = []
    b = []
    for line in open(instruments, 'r'):
        divide = line.split(',')
        a.append(divide[0])
        b.append(divide[-1].strip())

    for line1, line2 in zip(a, b):
        answer[line1] = line2

    if len(a) != len(set(a)):
        raise AssertionError('invalid boxes')
    if len(b) != len(set(b)):
        raise AssertionError('invalid boxes')
    if sorted(a) != sorted(b):
        raise AssertionError('invalid boxes')

    return answer

def cycle(thing, answer):
    """
    >>> boxes = read_boxes('boxes01.txt')
    >>> cycle('guitar', boxes)
    ('guitar', 'conga', 'maracas', 'synthesizer', 'trumpet')
    >>> cycle('saxophone', boxes)
    ('saxophone', 'banjo', 'drum set')
    >>> cycle('bass guitar', boxes)
    ('bass guitar', 'trombone')
    >>> cycle('clarinet', boxes)
    Traceback (most recent call last):
    AssertionError: invalid item
    """
    answer2 = [thing]

    if thing not in answer:
        raise AssertionError('invalid item')

    for key in answer:
        if thing in answer:
            if answer[thing] not in answer2:
                answer2.append(answer[thing])
                thing = answer[thing]
        if answer[thing] in answer2:
            break

    return tuple(answer2)

def longest_cycle(answer):
    """
    >>> boxes = read_boxes('boxes01.txt')
    >>> longest_cycle(boxes)
    5
    """
    comparing = []
    for l in answer:
        answer2 = cycle(l, answer)
        comparing.append(len(answer2))

    answer3 = max(comparing)
    return answer3


