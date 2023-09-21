class Cipher:
    """
    >>> cipher = Cipher('ABCD', '1AX3S1M2PYZ')
    >>> cipher.grid
    [['-', 'A', 'X', '-'], ['-', '-', 'S', '-'], ['M', '-', '-', 'P'], ['Y', 'Z', '-', '-']]
    >>> cipher.map
    {'A': 'AB', 'X': 'AC', 'S': 'BC', 'M': 'CA', 'P': 'CD', 'Y': 'DA', 'Z': 'DB'}
    >>> cipher.encode('spam')
    'BCCDABCA'
    >>> cipher.decode('BCCDABCA')
    'SPAM'
    >>> cipher.encode('eggs')
    Traceback (most recent call last):
    AssertionError: invalid message
    >>> cipher.decode('BCCDBACA')
    Traceback (most recent call last):
    AssertionError: invalid message

    >>> cipher02 = Cipher('HISPAYMENT', '14K1S2DL1NW4P2R1H3T3U2O6X3A1F6B1G4I1C2V1Y3E2M2J')
    >>> cipher02.grid
    [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', 'K', '-', 'S', '-', '-', 'D'], ['L', '-', 'N', 'W', '-', '-', '-', '-', 'P', '-'], ['-', 'R', '-', 'H', '-', '-', '-', 'T', '-', '-'], ['-', 'U', '-', '-', 'O', '-', '-', '-', '-', '-'], ['-', 'X', '-', '-', '-', 'A', '-', 'F', '-', '-'], ['-', '-', '-', '-', 'B', '-', 'G', '-', '-', '-'], ['-', 'I', '-', 'C', '-', '-', 'V', '-', 'Y', '-'], ['-', '-', 'E', '-', '-', 'M', '-', '-', 'J', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
    >>> cipher02.map
    {'K': 'IA', 'S': 'IM', 'D': 'IT', 'L': 'SH', 'N': 'SS', 'W': 'SP', 'P': 'SN', 'R': 'PI', 'H': 'PP', 'T': 'PE', 'U': 'AI', 'O': 'AA', 'X': 'YI', 'A': 'YY', 'F': 'YE', 'B': 'MA', 'G': 'MM', 'I': 'EI', 'C': 'EP', 'V': 'EM', 'Y': 'EN', 'E': 'NS', 'M': 'NY', 'J': 'NN'}
    >>> cipher02.encode('Have Marble and Coyle telegraph for influential men from Delaware and Virginia.')
    'PPYYEMNSNYYYPIMASHNSYYSSITEPAAENSHNSPENSSHNSMMPIYYSNPPYEAAPIEISSYESHAINSSSPEEIYYSHNYNSSSYEPIAANYITNSSHYYSPYYPINSYYSSITEMEIPIMMEISSEIYY'
    >>> cipher02.decode('PPYYEMNSNYYYPIMASHNSYYSSITEPAAENSHNSPENSSHNSMMPIYYSNPPYEAAPIEISSYESHAINSSSPEEIYYSHNYNSSSYEPIAANYITNSSHYYSPYYPINSYYSSITEMEIPIMMEISSEIYY')
    'HAVEMARBLEANDCOYLETELEGRAPHFORINFLUENTIALMENFROMDELAWAREANDVIRGINIA'
    >>> cipher02.encode('Indications of weakening here.')
    'EISSITEIEPYYPEEIAASSIMAAYESPNSYYIANSSSEISSMMPPNSPINS'
    >>> cipher02.decode('EISSITEIEPYYPEEIAASSIMAAYESPNSYYIANSSSEISSMMPPNSPINS')
    'INDICATIONSOFWEAKENINGHERE'
    >>> cipher02.encode('Press advantage and watch Board.')
    'SNPINSIMIMYYITEMYYSSPEYYMMNSYYSSITSPYYPEEPPPMAAAYYPIIT'
    >>> cipher02.decode('SNPINSIMIMYYITEMYYSSPEYYMMNSYYSSITSPYYPEEPPPMAAAYYPIIT')
    'PRESSADVANTAGEANDWATCHBOARD'
    """
    def __init__(self, grid_row, information):
        self.grid_row = grid_row
        self.information = information



    @property #
    def grid(self):
        length = len(self.grid_row)
        line = []
        answer = []
        for i, letter in enumerate(self.information):
            if letter.isdigit():
                if i < len(self.information) - 1:
                    if self.information[i].isdigit() and self.information[i + 1].isdigit():
                        letter = self.information[i] + self.information[i + 1]
                        for i in range(int(letter)):
                            line.append('-')
                            if len(line) == length:
                                answer.append(line)
                                line = []
                    elif self.information[i - 1].isdigit() and self.information[i + 1].isalpha():
                        pass
                    else:
                        for i in range(int(letter)):
                            line.append('-')
                            if len(line) == length:
                                answer.append(line)
                                line = []
            else:
                line.append(letter)
                if len(line) == length:
                    answer.append(line)
                    line = []
                elif (i + 1) == len(self.information):
                    for i in range(length - len(line)):
                        line.append('-')
                    answer.append(line)
                    line = []
        if len(answer) != length:
            for i in range(length - len(answer)):
                for i2 in range(length):
                    line.append('-')
                answer.append(line)

        return answer

    @property
    def map(self):
        info = self.grid
        row_value = ''
        value_l = []
        key_l = []
        answer = {}
        for v_rows, line in zip(self.grid_row, info):
            for h_rows, letter in zip(self.grid_row, line):
                if letter.isalpha():
                    row_value += v_rows + h_rows
                    value_l.append(row_value)
                    row_value = ''
                    key_l.append(letter)
        for l, l2 in zip(key_l, value_l):
            answer[l] = l2

        return answer

    def encode(self, word):
        dictionary = self.map
        answer = ''
        for l in word.upper():
            for key, value in dictionary.items():
                if key == l:
                    answer += value
        c = 0
        for l in word:
            if l.isalpha():
                c += 1

        if int(c * 2) != len(answer):
            raise AssertionError('invalid message')
        else:
            return answer

    def decode(self, code):
        dictionary = self.map
        dictionary2 = {}
        answer = ''
        for key, value in dictionary.items():
            dictionary2[value] = key

        sample = ''
        for l in code:
            sample += l
            if len(sample) == 2:
                for key, value in dictionary2.items():
                    if key == sample:
                        answer += value
                        sample = ''
        c = 0
        for l in code:
            if l.isalpha():
                c += 1
        if (c / 2) != len(answer):
            raise AssertionError('invalid message')
        else:
            return answer

