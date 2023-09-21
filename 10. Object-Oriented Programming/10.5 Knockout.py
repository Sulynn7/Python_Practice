def letter_frequencies(country):
    """
    >>> letter_frequencies('Russia')
    {'R': 1, 'U': 1, 'S': 2, 'I': 1, 'A': 1}
    >>> letter_frequencies('Moscou')
    {'M': 1, 'O': 2, 'S': 1, 'C': 1, 'U': 1}
    >>> letter_frequencies('Puerto Rico')
    {'P': 1, 'U': 1, 'E': 1, 'R': 2, 'T': 1, 'O': 2, 'I': 1, 'C': 1}
    >>> letter_frequencies('Guinea-Bissau')
    {'G': 1, 'U': 2, 'I': 2, 'N': 1, 'E': 1, 'A': 2, 'B': 1, 'S': 2}
    """
    c = 0
    answer = {}
    country2 = country.upper()
    for l in country2:
        if l.isalpha():
            for s in country2:
                if l == s:
                    c += 1
            answer[l] = c
            c = 0

    return answer


class Knockout:
    """
    >>> tournament = Knockout('../Term2/countries.csv')
    >>> tournament.capital('Switzerland')
    'Bern'
    >>> tournament.capital('Estonia')
    'Tallinn'
    >>> tournament.ordinary_time('Switzerland', 'Estonia')
    (5, 2)
    >>> tournament.ordinary_time('Belgium', 'Denmark')
    (2, 2)
    >>> tournament.ordinary_time('Portugal', 'Austria')
    (1, 2)
    >>> tournament.ordinary_time('Netherlands', 'Lithuania')
    (3, 3)
    >>> tournament.extra_time('Belgium', 'Denmark')
    (3, 2)
    >>> tournament.extra_time('Netherlands', 'Lithuania')
    (4, 5)
    >>> tournament.match('Switzerland', 'Estonia')
    'Switzerland'
    >>> tournament.match('Belgium', 'Denmark')
    'Belgium'
    >>> tournament.match('Portugal', 'Austria')
    'Austria'
    >>> tournament.match('Netherlands', 'Lithuania')
    'Lithuania'
    >>> tournament.winner(['Switzerland', 'Estonia', 'Belgium', 'Denmark', 'Portugal', 'Austria', 'Netherlands', 'Lithuania'])
    'Switzerland'
    """
    def __init__(self, all_file):
        reader = open(all_file, 'r')
        data = reader.readlines()
        answer = []
        for l in data:
            answer.append(l.strip('\n'))
        self.all_info = answer

    def capital(self, country):
        each_info = []
        for line in self.all_info:
            divide = line.split(',')
            each_info.append(divide)
        for i, line in enumerate(each_info):
            if country.upper() == line[0].upper():
                return line[1]
            else:
                if (i + 1) == len(each_info):
                    raise AssertionError('unknown country')

    def ordinary_time(self, country1, country2):
        capital1 = self.capital(country1)
        capital2 = self.capital(country2)
        if capital1 == AssertionError or capital2 == AssertionError:
            raise AssertionError('unknown country')
        else:
            answer = []
            first = 0
            for key, value in letter_frequencies(country1).items():
                for k, v in letter_frequencies(capital2).items():
                    if key == k:
                        small_num = min(value, v)
                        first += small_num
            answer.append(first)
            second = 0
            for key, value in letter_frequencies(country2).items():
                for k, v in letter_frequencies(capital1).items():
                    if key == k:
                        small_num = min(value, v)
                        second += small_num
            answer.append(second)
            return tuple(answer)

    def extra_time(self, country1, country2):
        capital1 = self.capital(country1)
        capital2 = self.capital(country2)
        a = self.ordinary_time(country1, country2)
        if capital1 == AssertionError or capital2 == AssertionError:
            raise AssertionError('unknown country')

        answer = []
        first = 0
        for key, value in letter_frequencies(country1).items():
            for k, v in letter_frequencies(capital2).items():
                if key == k:
                    total = value * v
                    first += total
        answer.append(first)
        second = 0
        for key, value in letter_frequencies(country2).items():
            for k, v in letter_frequencies(capital1).items():
                if key == k:
                    total = value * v
                    second += total
        answer.append(second)
        return tuple(answer)

    def match(self, country1, country2):
        result = self.ordinary_time(country1, country2)
        if result[0] == result[-1]:
            result2 = self.extra_time(country1, country2)
        else:
            result2 = result
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        order = []
        if result2[0] == result2[-1]:
            if country1[0].upper() == country2[0].upper():
                for i, l in enumerate(alphabet):
                    if l.upper() == country1[1].upper():
                        order.append(i)
                for i, l in enumerate(alphabet):
                    if l.upper() == country2[1].upper():
                        order.append(i)
            else:
                for i, l in enumerate(alphabet):
                    if l.upper() == country1[0].upper():
                        order.append(i)
                for i, l in enumerate(alphabet):
                    if l.upper() == country2[0].upper():
                        order.append(i)
            if order[0] < order[-1]:
                return country1
            else:
                return country2
        else:
            big = max(result2)
            if big == result2[0]:
                return country1
            else:
                return country2

    def winner(self, game_countries):
        winning_country = []
        c = 1
        d = 0
        for i in range(len(game_countries)):
            d += 1
            c *= 2
            if c == len(game_countries):
                break
        for i in range(d):
            for i, word in enumerate(game_countries):
                if (i + 1) % 2 == 0:
                    win = self.match(game_countries[i - 1], game_countries[i])
                    winning_country.append(win)
            game_countries = winning_country
            if len(winning_country) == 1:
                for l in winning_country:
                    return l
            else:
                winning_country = []