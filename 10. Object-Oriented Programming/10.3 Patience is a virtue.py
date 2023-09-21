class PatienceSorter:
    """
    >>> sorter = PatienceSorter()
    >>> sorter.stacks()
    []
    >>> sorter.stack_count()
    0
    >>> sorter.add_item(4).stacks()
    [[4]]
    >>> sorter.stack_count()
    1
    >>> sorter.add_item(3).stacks()
    [[3, 4]]
    >>> sorter.add_item(9).stacks()
    [[3, 4], [9]]
    >>> sorter.stack_count()
    2
    >>> sorter.add_item(1).stacks()
    [[1, 3, 4], [9]]
    >>> sorter.add_item(5).stacks()
    [[1, 3, 4], [5, 9]]
    >>> sorter.add_item(2).stacks()
    [[1, 3, 4], [2, 5, 9]]
    >>> sorter.add_item(7).stacks()
    [[1, 3, 4], [2, 5, 9], [7]]
    >>> sorter.stack_count()
    3
    >>> sorter.add_item(8).stacks()
    [[1, 3, 4], [2, 5, 9], [7], [8]]
    >>> sorter.add_item(6).stacks()
    [[1, 3, 4], [2, 5, 9], [6, 7], [8]]
    >>> sorter.stack_count()
    4
    >>> sorter.item_count()
    9
    >>> sorter.remove_item()
    1
    >>> sorter.stacks()
    [[3, 4], [2, 5, 9], [6, 7], [8]]
    >>> sorter.remove_item()
    2
    >>> sorter.stacks()
    [[3, 4], [5, 9], [6, 7], [8]]
    >>> sorter.remove_item()
    3
    >>> sorter.stacks()
    [[4], [5, 9], [6, 7], [8]]
    >>> sorter.remove_item()
    4
    >>> sorter.stacks()
    [[5, 9], [6, 7], [8]]
    >>> sorter.stack_count()
    3
    >>> sorter.remove_item()
    5
    >>> sorter.stacks()
    [[9], [6, 7], [8]]
    >>> sorter.remove_item()
    6
    >>> sorter.stacks()
    [[9], [7], [8]]
    >>> sorter.remove_item()
    7
    >>> sorter.stacks()
    [[9], [8]]
    >>> sorter.remove_item()
    8
    >>> sorter.stacks()
    [[9]]
    >>> sorter.remove_item()
    9
    >>> sorter.stacks()
    []
    >>> sorter.remove_item()
    Traceback (most recent call last):
    AssertionError: no more items

    >>> sorter = PatienceSorter()
    >>> sorter.add_items([7, 5, 2, 1, 8, 6, 3, 9, 4]).stacks()
    [[1, 2, 5, 7], [3, 6, 8], [4, 9]]
    >>> sorter.stack_count()
    3
    >>> sorter.item_count()
    9
    >>> sorter.remove_items()
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> sorter.stacks()
    []
    >>> sorter.stack_count()
    0
    >>> sorter.item_count()
    0
    """
    def __init__(self):
        self.answer = []

    def stacks(self):
        return self.answer

    def stack_count(self):
        return len(self.answer)

    def item_count(self):
        a = []
        for i in self.answer:
            for k in i:
                a.append(k)
        return len(a)

    def add_item(self, number):
        if self.stack_count() == 0:
            new_stack1 = []
            new_stack1.append(number)
            self.answer.append(new_stack1)

        else:
            c = 0
            for l in tuple(self.answer):
                if number <= min(l):
                    l.append(number)
                    c += 1
                    break

            if c == 0:
                new_stack2 = []
                new_stack2.append(number)
                self.answer.append(new_stack2)

        new_answer = []
        for i, l in enumerate(self.answer):
            l = sorted(l)
            new_answer.append(l)
            self.answer = new_answer
        return self

    def remove_item(self):
        all = []
        if self.stack_count() == 0:
            raise AssertionError('no more items')

        for l in self.answer:
            for k in l:
                all.append(k)
        for a in self.answer:
            if min(all) in a:
                a.remove(min(all))
                break
        for b in self.answer:
            if len(b) == 0:
                self.answer.remove(b)

        return min(all)

    def add_items(self, long):
        answers = []

        for i in long:
            t = self.add_item(i)
            answers.append(t)

        return self

    def remove_items(self):
        removed_answer = []
        c = 0
        for l in self.answer:
            for k in l:
                c += 1
        for i in range(c):
            a = self.remove_item()
            removed_answer.append(a)

        return tuple(removed_answer)
