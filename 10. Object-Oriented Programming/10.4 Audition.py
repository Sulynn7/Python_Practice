class Collection:
    """
    >>> A = Collection([33, [27, 30], 32, 25, [20, 24], 31, 19])
    >>> A.numbers()
    {19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33}
    >>> len(A)
    14
    >>> A.normalform()
    [[19, 25], [27, 33]]
    >>> print(A)
    [[19, 25], [27, 33]]
    >>> A
    Collection([[19, 25], [27, 33]])

    >>> B = Collection([22, 26, 30])
    >>> A - B
    Collection([[19, 21], [23, 25], [27, 29], [31, 33]])
    >>> B - A
    Collection([26])
    >>> A | B
    Collection([[19, 33]])
    >>> A & B
    Collection([22, 30])
    >>> A ^ B
    Collection([[19, 21], [23, 29], [31, 33]])

    >>> C = Collection([[1, 5], [7, 7]])
    >>> D = Collection([[1, 5], [7, 8]])
    >>> C == Collection([1, 2, 3, 4, 5, 7])
    True
    >>> C == D
    False
    >>> C != D
    True
    >>> C < D
    True
    >>> C <= D
    True
    >>> C > D
    False
    >>> C >= D
    False
    >>> D > C
    True
    >>> D >= C
    True
    """
    def __init__(self, numbers):
        self.number = numbers

    def __repr__(self):
        return f'Collection({self.normalform()})'

    def __str__(self):
        return f'{self.normalform()}'

    def __len__(self):
        return len(self.numbers())

    def numbers(self):
        new_tool = []
        for n in self.number:
            if type(n) == int:
                new_tool.append(n)
            else:
                c = 0
                n = list(n)
                diff = n[-1] - n[0]
                new_tool.append(n[0])
                for i in range(diff):
                    new_tool.append(n[0] + c)
                    c += 1
                new_tool.append(n[-1])
        self.num = new_tool

        return set(self.num)

    def normalform(self):
        a = sorted(list(self.numbers()))
        if a == []:
            return []
        else:
            c = a[0]
            new = []
            normal = []
            d = a[0]
            for i, l in enumerate(a):
                if l != c:
                    new.append(d)
                    new.append(c - 1)
                    if new[0] == new[-1]:
                        normal.append(d)
                    else:
                        normal.append(new)
                    c = l
                    d = l
                if i + 1 == len(a):
                    new2 = []
                    new2.append(d)
                    new2.append(a[-1])
                    if new2[0] == new2[-1]:
                        normal.append(d)
                    else:
                        normal.append(new2)

                c += 1

                if len(new) == 2:
                    new = []
            return normal

    def __sub__(self, other):
        wide = self.numbers()
        wide2 = other.numbers()
        wide3 = []
        for l in list(wide):
            if l not in list(wide2):
                wide3.append(l)
        self.number = wide3
        answer = self.normalform()
        self.number = wide
        return Collection(answer)

    def __or__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        wide3 = set(wide1 + wide2)
        self.number = wide3
        answer = self.normalform()
        self.number = wide1
        return Collection(answer)

    def __and__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        wide3 = []
        for l in wide2:
            if l in wide1:
                wide3.append(l)
        self.number = wide3
        answer = self.normalform()
        self.number = wide1
        return Collection(answer)

    def __xor__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        wide3 = []
        for l in wide1:
            if l not in wide2:
                wide3.append(l)
        for l in wide2:
            if l not in wide1:
                wide3.append(l)
        self.number = wide3
        answer = self.normalform()
        self.number = wide1
        return Collection(answer)

    def __eq__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        if wide1 == wide2:
            return True
        else:
            return False

    def __ne__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        if wide1 != wide2:
            return True
        else:
            return False

    def __lt__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        c = 0
        for l in wide1:
            if l in wide2:
                c += 1
        if c == len(wide1):
            if len(wide1) < len(wide2):
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        c = 0
        for l in wide1:
            if l in wide2:
                c += 1
        if c == len(wide1):
            if len(wide1) <= len(wide2):
                return True
            else:
                return False
        else:
            return False
    def __gt__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        c = 0
        for l in wide2:
            if l in wide1:
                c += 1
        if c == len(wide2):
            if len(wide1) > len(wide2):
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        wide1 = list(self.numbers())
        wide2 = list(other.numbers())
        c = 0
        for l in wide2:
            if l in wide1:
                c += 1
        if c == len(wide2):
            if len(wide1) >= len(wide2):
                return True
            else:
                return False
        else:
            return False
