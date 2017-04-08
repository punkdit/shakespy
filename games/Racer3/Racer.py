#!/usr/bin/python3


import os, sys
from time import sleep

_print = print
def print(*args, **kw):
    _print(*args, **kw)
    sys.stdout.flush()

_input = input
def input(*args, **kw):
    print(*args, **kw)
    return _input()



import pickle
from time import sleep as sh
from random import randint as d, choice
from Racer_data import *



Heart = True


class U(object):

    def __init__(self, name):

        self.name = name
        self.bets = 2
        self.money = 23
        self.day = 0
        self.bet = 0
        self.clued = 0
        self.clues = ['Clue #']
        self.continues = 0
        self.met = 0
        self.someone = 'Hmm'
        self.meetnext = []
        self.ticket = {}
        self.doors = {
                        1: 'bag', 2: 'guide', 3: 'bookie',
                        4: 'garden', 5: 'track', 6: 'sleep',
                        9: 'options'}
        self.flags = {
                        'guide': 1, 'bookie': 1, 'garden': 0,
                        'track': 0, 'sleep': 1, 'options': 1}
        self.meet = {
                        1: ['May Lee', 0], 2: ['Wong', 0],
                        3: ['Travis', 0], 4: ['Pauly', 0],
                        5: ['Chang', 0]}
        self.bag = {
                        'pillow': 1, 'comb': 1}


class Horse(object):

    D = {}

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
        self.secret = (self.weakness % 4) + 2
        self.runs = 0
        self.stars = 0
        self.trackpoints = 0
        self.badges = []

    def __repr__(self):
        return self.name

    def raisin(self, value, amount):
        if value in ['sp', 'speed', 'both']:
            self.speed += amount
        if value in ['st', 'strength', 'both']:
            self.strength += amount
        self.rank -= amount
        if self.rank < 1: self.rank = 1
        if self.rank == 1:
            self.Star('Rank 1')

    def Star(self, badge):
        if badge not in self.badges:
            self.badges.append(badge)
            self.stars += 1


def weather():

    temp = d(7, 42)
    rains = d(0, 3)

    if temp < 17: feel = 'cool'
    elif temp > 23: feel = 'warm'
    else: feel = 'mild'

    dirt = ['dry', 'soft', 'damp', 'wet'][rains]
    sky = ['clear', 'breezy', 'cloudy', 'rainy'][rains]

    u.weather = {'temp': temp, 'feel': feel,
                    'dirt': dirt, 'sky': sky}


def clr():

    #print('\n' * 100)
    print("CLEAR")


def bag():

    clr()

    print("\n        You own..\n")

    for k, v in u.bag.items():
        if v < 1: continue
        if v > 1: v = "(" + str(v) + ")"
        else: v = " "
        print('                ', k, v)

    return menu


def flag(flag):

    u.flags[flag] = 1

    day = 'done'  #maybe.. let's check..

    for v in u.flags.values():
        if v == 0:
            day = 'notdone'; break

    if day == 'done':
        u.flags['sleep'] = 0  #time for bed


def raceroutine():

    pass


def race():

    #here we go!

    clr()

    print('On this', u.weather['feel'] +
            ',', u.weather['sky'], u.today + '...')

    print('We have', u.horses_per, 'racers.')

    for horse, bet in u.ticket.items():
        if bet == 1: money = 'dollar'
        else: money = 'dollars'
        print('\nYou have', bet, money, 'bet on', horse)

    print()

    input('\nReady? \n')

    clr()

    sh(2)
    print('    The horses are led into their stalls.')
    sh(3)

    #weakness 1 - hot, 2 - wet, 3 - inside, 4 - outside
    for lane, horse in u.lanes.items():

        print('\n  ', horse, 'enters stall', lane)
        sh(2)
        if (u.horses_per - lane < 2 and horse.weakness == 4) \
        or (lane < 3 and horse.weakness == 3):
            print('        There is a little delay as',
                        horse, 'resists')
            sh(4)
        elif horse.weakness == 1 and u.weather['temp'] > 26:
            print('        There is a little delay..',
                        horse, 'looks a little weak..')
            sh(4)
        elif horse.weakness == 2 and u.weather['dirt'] == 'wet':
            print('        There is a little delay..',
                        horse, 'is taking its time..')
            sh(4)
    sh(3)
    print('''

                The horses are in the blocks..

                We're awaiting the starting gun..

                ''')
    sh(2)
    for i in range(d(3,7)):
        print('.',)
        sh(1.2)

    print('\n\n                !! Honk !!')
    sh(2)
    print('\nThe stall gates open and the horses are off and racing!')
    sh(2)

    raceroutine()


def sleep():

    input('\n sleep time..')

    for flag in u.flags: u.flags[flag] = 0
    u.flags['guide'] = 1
    u.flags['bookie'] = 1

    return game


def track():

    clr()

    if u.bet == 0:  #if no bet yet, track conditions..
        print('track details..\n')
        print('    track:', u.weather['dirt'])
        print('    weather:', u.weather['feel'], u.weather['sky'])
        flag('track') #track now closes until bet made
        return menu

    race()

    input('\n amazing race...')

    flag('track')  #after race, track closes access for the day

    u.flags['bookie'] = 0  #bookie opens again

    return menu


def clue():

    something = ("\nDid you know it's already " +
                "into the 26th century in Buddhism?\n")

    if u.clued == 1:
        u.clued = 0
        u.met = 0

    if u.met == 0:

        u.meetnext = [] #make a list  of unmet people

        for person in u.meet:
            if u.meet[person][1] == 0:
                u.meetnext.append(person)

    if u.someone == 'May Lee': they = 'She'
    else: they = 'He'

    if u.met == 0:
        they = 'The person'
        someone = 'a person'
    else: someone = u.someone

    if len(u.meetnext) == 0: #no more unmet peeps, all done
        u.clued == 2
        u.met = 2
        flag('options')
        return something
    elif u.met == 0:
        meet = choice(u.meetnext)
        u.meetnext.remove(meet)
        u.meet[meet][1] = 1
        u.someone = u.meet[meet][0]
        u.met = 1

    print('''
You see {0} sitting on a wooden bench.
    {1} gestures. You approach.'''.format(someone, they))

    if someone == 'a person':
        print("    {} says: I have a clue for you".format(they))
        print('\n        My name is', u.someone)
        print("    Come see me when you're ready")
        u.bag['clues'] = 1
    else:
        print('    {} asks: '.format(they) +
            'Have you got the answer yet?')

    something = '\nYou keep the clue in your pocket..\n'

        #to do, to do, to do, to dooo, to dooo
    silver = input('\nSolve the clue? y/n -> ')
    if 'y' in silver.lower():
        u.clued == 1
        u.met = 0
        u.bag['clues'] = 0
        something = "Cool bananas!"

    flag('options')
    flag('garden')

    return something


def garden():

    clr()

    print ('''

    Outside your home on the east of the tunnel..

This is a special garden area,
    created by the local Chinese community

    Many lovely trees to sit under

        Nice place to meditate and think

        ''')

    if u.money < 1 and u.bet != 1:
        lucky = d(2, 5)
        print('    You find', lucky, 'dollars.')
        u.money += lucky

    if u.bet == 0 and u.flags['guide'] == 1:
        print('''

    You find today's newspaper sitting on a wooden bench.
        The story of the criminal underworld war continues...
        There is a racing guide in the paper. You take it.

        ''')

        u.bag['guide'] = 1
        u.flags['guide'] = 0
        u.flags['bookie'] = 0

    if u.bet == 1 and u.flags['track'] == 1 \
        and u.flags['bookie'] == 1:

            something = clue()
            input(something)

    return menu


def lanes():

    u.lanes = {} #dic of lanenum: horseinstance

    for lane, horsenum in u.racing.items():

        u.lanes[lane] = Horse.D[horsenum]

        u.lanes[lane].lane = lane

        u.lanes[lane].notice = " "

        if u.lanes[lane].stars > 0:
            u.lanes[lane].notice = "*"


def printlanes():

    for lane in u.lanes:

        print('Lane %02d' % lane,
            '- Horse %02d -' % u.lanes[lane].number,
            u.lanes[lane].name, u.lanes[lane].notice)


def guide():

    clr()

    print(u.today)

    print("\nLet's see who's racing today..\n")

    printlanes()

    lane = 23

    print("\nEnter lane number to view horse details")

    while lane - 1 not in range(u.horses_per):
        if lane == 0: break
        try: lane = int(input("type 0 to close guide\n"))
        except: continue

    if lane != 0:
        return bio(lane)

    clr()
    return menu


def betdone():

    u.bet = 1
    u.flags['track'] = 0
    flag('bookie')
    print('\nYou no longer need the guide.')
    print('\nYou trash it on the way out of the bookie tent.')
    del u.bag['guide']
    flag('guide')


def bet(lane):

    horse = u.lanes[lane]

    while True:

        print('\nYou are betting on {}'.format(horse.name))

        print('Enter 0 to cancel bet')

        saymoney()

        try:
            bet = int(input('\nHow much to bet? '))
        except:
            print('''
                We cannot accept cents for bets.
                We apologise for the inconvenience.
                Only whole numbers please.
                        ''')
            continue

        if bet > u.money:
            print("\n    You don't have enough money")
            continue

        if bet < 0:
            print("\n    That doesn't work")
            continue

        if bet == 0: return ticket

        u.ticket[horse] = bet

        u.money -= bet

        print('\n        Ticket:', u.ticket)

        if len(u.ticket) < u.bets and u.money >= 1:
            print('\n    You may bet on another horse')
            a = input('    Enter 1 to bet again.  ')
            if a == '1':
                return ticket

        betdone()

        return menu


def ticket():

    saymoney()

    print('\nEnter lane number to bet on horse')

    print(u.lanes)

    lane = 23

    while lane - 1 not in range(u.horses_per):
        if lane == 0: break
        try:
            lane = int(input("type 0 to close betting\n"))
            if u.lanes[lane] in u.ticket.keys():
                print('\n    You have bet on that horse already')
                print('    Choose another one..\n')
                print(u.lanes)
                lane = 23
                continue
        except: continue

    if lane != 0:
        return bet(lane)

    if len(u.ticket) == 0: return menu

    print(u.ticket)

    betdone()

    return menu


def bookie(extras=0):
    '''for key, value in extras: maybe
    financial functions'''

    clr()

    if u.bet != 1:
        bet = input('\nTalk to bookie. Get scoop. Bet money.. OK?  ')
        if bet not in 'yesYes': return menu
        return ticket
    else:
        input('\nCheck winnings. Collect. Ok? ')
        flag('bookie')

    return menu


def saymoney():

    if int(u.money) == 1: money = 'dollar'
    else: money = 'dollars'
    print ('\nYou have', u.money, money)


def bio(lane):

    clr()

    horse = u.lanes[lane]

    print ("Horse number {0}, {1}, doesn't like".format(
                horse.number, horse.name))

    if horse.weakness in [1, 2]:
        print ('{} weather.'.format(
               Horse.weaknesses[horse.weakness]))
    else:
        print ('{} lanes.'.format(
                Horse.weaknesses[horse.weakness]))

    print('Horse rank:', horse.rank)

    if len(horse.badges) == 0:
        print('\nNo badges')
    else:
        print('Horse stars:', horse.stars)
        for badge in horse.badges: print ('*', badge)

    input('\nOk? ')

    return guide

    #horse info

    #runs

    #badges

    #weakness


def chooseHorses(numhorses):

    gamehorses = []

    while len(gamehorses) < numhorses:
        randhorse = choice(Horselist()).strip()
        if randhorse in gamehorses: continue
        gamehorses.append(randhorse)

    return gamehorses


def game_over():

    global Heart

    clr()

    decision = input('''

                 ___ Game Over ___

                Quit or Start Again



                        ''')

    if 'q' in decision.lower():
        Heart = False

    print(); sh(1); print(); sh(2)
    return main


def menu():

    print()

    for num, door in u.doors.items():

        if door in u.flags and u.flags[door] == 1: continue

        print(' {0} - {1}'.format(num, door))

    while True:

        try:
            path = int(input('\n '))
        except:
            continue

        if path == 1: return bag

        if (path in u.doors.keys()
            and u.doors[path] in u.flags.keys()
            and u.flags[u.doors[path]] == 0):
                go = eval(u.doors[path])
                return go

        else: continue


def day():

    clr()

    print('Day {0} - {1}'.format(u.day, u.today))

    print('''

Good morning.

    You stuff your bag, cleaning your sleeping area.

    You finish your bottle of water,
        you run a comb through your hair.

    It's time to fly


            ''')

    sh(2)
    return menu


def racing():

    u.racing = {} #dic of lanenum: horsenum

    lane = 0

    while len(u.racing) < u.horses_per:
        roll = d(1, u.numhorses)
        if roll in u.racing.values():
            continue
        lane += 1
        u.racing[lane] = roll


def news():

    #stuff about stuff
    print('Newsy newsy newsy news...')


def save():

    clr()

    wannasave = input('Saving, ok?  ')
    if 'n' in wannasave.lower(): return options

    flag('options')

    u.horsedata = Horse.D

    with open('save.dat', 'wb') as data:
        pickle.dump(u, data)

    message = 'Saved, ' + u.name + '.. Continue game or quit?\n'
    saved = input(message)
    if 'q' in saved.lower(): return game_over

    clr()

    return menu


def load():

    global u

    clr()

    wannaload = input('Loading, ok?  ')
    if 'n' in wannaload.lower(): return options

    with open('save.dat', 'rb') as data:
        u = pickle.load(data)

    Horse.D = u.horsedata
    Horse.counter = len(u.gameHorses)
    loaded = 'Loaded.. Welcome back, ' + u.name
    input(loaded)

    flag('options')
    clr()
    sh(1)

    for horse in u.horsedata.values():

        print('Importing..')
        print(format(horse.number, '02d'), horse.name)
        print('Star:', horse.rank)
        print('---------------------------------')
        sh(0.17)

    sh(2)
    clr()
    return menu


def options():

    clr()

    print('''

                =---------------------------=
                 = Watcha watcha wanna do? =
                =---------------------------=


            1 - Resume
            4 - Load
            6 - Save
            9 - Quit

        ''')

    while True:

        try: i = int(input('\n ? '))
        except: continue

        if i not in [1, 4, 6, 9]: continue

        if i == 9: return game_over

        if i == 6: return save

        if i == 4: return load

        return menu


def broadcast():

    weekday = u.day % 7
    days = ['Sunday', 'Moonday', 'Marsday', 'Mercuryday',
            'Jupiterday', 'Venusday', 'Saturnday']
    u.today = days[weekday]

    print ('''

        The alarm goes off. The alarm goes on.

    On comes the morning radio broadcast..


            ''')

    print(u.today)

    weather()

    print('\nThe temperature today is',
            u.weather['temp'], 'degrees.')

    print("It's", u.weather['feel'], 'and',
            u.weather['sky'] + '.')

    print()

    #clue things about garden

    news()

    #print('Racing today:')

    racing()

    lanes()

    #printlanes()

    print()

    i = input("Very interesting, wouldn't you say?\n")

    print('indeed..', i)


def game():

    clr()

    u.bet = 0

    u.ticket = {}

    flag('sleep')

    u.day += 1

    broadcast()

    return day


def intro():

    clr()

    print ('''
        -----/------\\
        ----| Racer! |
        -----\\------/

        You are nearly broke.
        Homeless.

        You've made camp at the skirts of the city..
        in an unused service tunnel..
        which connects the chinese tea garden
        with the race track.

        You hope to make a rags-to-riches story come true.

            ''')

    saymoney()

    input('\n Are you ready? \n\n    ')

    sh(2)
    return game


def main():

    global u, horse

    clr()

    print('\n    1 - New game\n    2 - Load')

    while True:
        try: hmm = int(input('\n? '))
        except: continue
        if hmm == 2: return load
        if hmm == 1: break
        continue

    you = input('Enter your name: ').strip()

    u = U(you)

    Horse.counter = 0

    u.races = ('\nHow many races, ' + u.name +
                '? (enter 1-5) \n')

    while u.races not in range(6) or u.races == 0:
        try: u.races = int(input(u.races))
        except: continue

    print('\nMaximize your window\n')

    u.horses_per = ('Horses per race, ' + u.name +
                    '? (enter 6-10) \n ')

    while u.horses_per not in range(11) or u.horses_per < 6:
        try: u.horses_per = int(input(u.horses_per))
        except: continue

    u.numhorses = u.horses_per * u.races

    u.gameHorses = chooseHorses(u.numhorses)

    for name in u.gameHorses:

        horse = Horse(name)  #instance creation!

        Horse.D[horse.number] = horse  #instance into dictionary

        print('Importing..')
        print(format(horse.number, '02d'), horse.name)
        print('Star:', horse.rank)
        print('---------------------------------')

        if horse.rank == 1:
            horse.Star('Golden Champion')
            horse.Star('Rank 1')
        elif horse.rank < 6:
            horse.Star('Born Champion')
        if horse.rank < 11:
            horse.Star('Top Ten Breed')
        sh(0.13)

    sh(2)
    return intro


def wonderwall():

    global Heart

    funk = main

    while Heart is True:

        load = funk()

        funk = load


wonderwall()
