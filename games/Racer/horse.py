from random import randint as d


class Horse:
    '''to make each horse an object'''

    counter = 0

    weaknesses = {1: 'hot', 2: 'wet', 3: 'inside', 4: 'outside'}

    def __init__(self, name):
        Horse.counter += 1
        self.number = Horse.counter
        self.name = name
        self.weakness = d(1, 4)
        self.strength = d(70, 90)
        self.speed = d(50, 80)
        self.rank = 171 - self.speed - self.strength
        self.secret = (self.weakness + 2) % 4 or 4
        self.runs, self.wins = 0, 0
        self.stars, self.trackpoints = 0, 0
        self.badges = []

    def __repr__(self):
        return self.name

    def rise(self, value, amount):
        '''change speed or strength or both at once'''

        if value in ['sp', 'speed', 'both']:
            self.speed += amount
            if self.speed >= 123:
                if self.wins:
                    self.star('Rocket')
                if self.strength < 100:
                    self.strength += 1

        if value in ['str', 'strength', 'both']:
            self.strength += amount
            if self.strength >= 132:
                if self.wins:
                    self.star('Rock')
                if self.speed < 111:
                    self.speed += 1

        self.rank -= amount // 2

        self.rank = max(self.rank, 1)
        if self.rank == 1:
            self.star('Rank 1')

    def star(self, badge):
        '''add achievement badge to horse'''
        if badge not in self.badges:
            self.badges.append(badge)
            self.stars += 1

