#! /usr/bin/python3

<<<<<<< HEAD
from __future__ import print_function
from time import sleep as s
from random import choice, randint as d
=======
import pickle
from time import sleep as sh
from random import randint as d, choice
>>>>>>> 5cd19fdc9aee780d7afe4767c25d344dd14b4077
from Racer_data import *
import pickle
#from ssserve import *



Heart = True


class U(object):

    def __init__(self, name):

        self.D = {}
        self.name = name
        self.wait = 0.1 #weeeeeee!
        self.bets = 2
        self.money = 23
        self.day = 0
        self.betyet = 0
        self.clued = 0
        self.clues = 0
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
        if self.secret == 5: self.secret = 1
        self.runs = 0
        self.wins = 0
        self.stars = 0
        self.trackpoints = 0
        self.badges = []

    def __repr__(self):
        return self.name

    def Rise(self, value, amount):
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

    dirt = ['hard', 'soft', 'damp', 'muddy'][rains]
    sky = ['clear', 'breezy', 'cloudy', 'rainy'][rains]

    u.weather = {'temp': temp, 'feel': feel,
                    'dirt': dirt, 'sky': sky}


def clr():

    print('\n' * 99)

    #print('CLEAR')


def gap(lines):

    print('\n' * lines)


def sh(secs):

    secs = secs * u.wait
    s(secs)


def bag():

    clr()
    print("\n        You own..\n")

    for k, v in u.bag.items():
        if v < 1: continue
        if v == 1: v = " "
        else: v = "(" + str(v) + ")"
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


def possy(horses):

    if u.seggy == 1:

        sortpossy = {}
        u.possy = []
        oddslist = []

        for horse in horses:
            while True:
                if horse.odds in sortpossy.keys():
                    horse.odds += 0.001
                else: break
            sortpossy[horse.odds] = horse

        for each in sortpossy.keys():
            oddslist.append(each)

        oddslist.sort()

        for oddz in oddslist:
            u.possy.append(sortpossy[oddz])

        h = u.horses_per - 1

        x = d(0, h)

        while True:
            y = d(0, h)
            if y != x:
                break

        print(u.possy)

        u.possy[x], u.possy[y] = u.possy[y], u.possy[x]

        print(u.possy)

    else:

        shuffler = {}

        for lane, horse in u.lanes.items():

            strength = horse.strength
            speed = horse.speed

            if (u.horses_per - lane < 2 and horse.weakness == 4) \
            or (lane < 3 and horse.weakness == 3):
                if d(0, 1) == 1:
                    horse.Rise('speed', 0 - d(2, 3))
                else: horse.Rise('speed', 1)
            elif horse.weakness == 1 and u.weather['temp'] > 26:
                if d(0, 1) == 1:
                    horse.Rise('both', 0 - d(1, 2))
                else: horse.Rise('both', 1)
            elif horse.weakness == 2 and u.weather['dirt'] == 'wet':
                if d(0, 1) == 1:
                    horse.Rise('str', 0 - d(1, 2))
                else: horse.Rise('str', 1)

            if (u.horses_per - lane < 2 and horse.secret == 4) \
            or (lane < 3 and horse.secret == 1):
                if d(0, 1) == 1:
                    horse.Rise('speed', d(1, 3))
                else: horse.Rise('speed', 1)
            elif horse.secret == 3 and u.weather['temp'] > 26:
                if d(0, 1) == 1:
                    horse.Rise('both', d(1, 3))
                else: horse.Rise('both', 1)
            elif horse.secret == 4 and u.weather['dirt'] == 'wet':
                if d(0, 1) == 1:
                    horse.Rise('str', d(1, 3))
                else: horse.Rise('str', 1)
            if u.seggy > 5 and horse.strength > 85:
                    horse.Rise('speed', 2)
                    horse.Rise('str', -2)

            horse.trackpoints += (horse.strength - strength)
            horse.trackpoints += (horse.speed - speed)

            print(horse.trackpoints)

            while True:
                if horse.trackpoints in shuffler.keys():
                    if d(0, 2) != 1:
                        horse.trackpoints += 0.1
                    else:
                        horse.trackpoints -= 0.1
                else: break

            shuffler[horse.trackpoints] = horse

        u.possy = []
        pointlist = []

        for each in shuffler.keys():
            pointlist.append(each)
        print(pointlist)
        pointlist.sort()

        for each in pointlist:
                u.possy.append(shuffler[each])

        u.possy.reverse()

        h = u.horses_per - 1

        x = d(0, h)

        while True:
            y = d(0, h)
            if y != x:
                break

        print(u.possy)

        u.possy[x], u.possy[y] = u.possy[y], u.possy[x]

        print(u.possy)

        diffs(horses)


def diffs(oldpossy):

    u.diffs = {}

    for pos, it in enumerate(u.possy):
        if it != oldpossy[pos]:
            u.diffs[it] = oldpossy.index(it) - pos

    #print (u.diffs)

    for k, v in u.diffs.items():
        if v > 0:
            print(k, 'jumps up', v, 'spots into position', u.possy.index(k)+1)
        else:
            print(k, 'drops', str(v)[1:],
            'spots into position', u.possy.index(k)+1)

    input('hmm...')


def raceroutine(segments):

    for segment in range(segments):
        u.seggy = segment + 1

        if u.seggy == segments:
            segger = 'last'
        else:
            segs = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth',
                    5: 'fifth', 6: 'sixth', 7: 'seventh'}
            segger = segs[u.seggy]

        if segger == 'first':
            possy(u.lanes.values())
        else: possy(u.possy)

        if segger == 'first':
            print('\nThe horses shake their legs..')
            print('and begin their equine dance across this',
                                u.weather['dirt'], 'track..\n')
            #print('on this', u.weather['feel'], u.today, 'afternoon')
            sh(1.5)
        elif segger == 'last':
            print('\nOh ho ho..')
            print('The final leg..')
            sh(1.5)

        print('\nInto the', segger, 'turn..')
        sh(1.5)

        for horsey in u.possy:
            print(horsey)
        sh(1.5)


def race():

    clr()
    print('On this', u.weather['feel'] +
            ',', u.weather['sky'], u.today + '...')
    print('We have', u.horses_per, 'racers.')

    for horse, bet in u.ticket.items():
        if bet == 1: money = 'dollar'
        else: money = 'bucks'
        print('\nYou have', bet, money, 'bet on', horse)

    input('\nReady? \n')

    clr()

    sh(2)
    print('    The horses are led into their stalls.')
    sh(3)

    #1 - hot, 2 - wet, 3 - inside, 4 - outside
    for lane, horse in u.lanes.items():

        print('\n  ', horse, 'enters stall', lane)
        sh(1.5)

        if (u.horses_per - lane < 2 and horse.weakness == 4) \
        or (lane < 3 and horse.weakness == 3):
            horse.Rise('speed', -7)
            if d(0, 1) == 1:
                print('        There is a little delay as',
                        horse, 'resists')
                horse.Rise('both', -3)
                sh(d(3, 5))
        elif horse.weakness == 1 and u.weather['temp'] > 26:
            horse.Rise('both', -5)
            if d(0, 1) == 1:
                print('        There is a little delay..',
                        horse, 'looks a little weak..')
                horse.Rise('both', -3)
                sh(d(3, 5))
        elif horse.weakness == 2 and u.weather['dirt'] == 'wet':
            horse.Rise('str', -7)
            if d(0, 1) == 1:
                print('        There is a little delay..',
                        horse, 'is taking its time..')
                horse.Rise('both', -3)
                sh(d(3, 5))
    sh(3)
    gap(5)
    print('''

                The horses are in the blocks..

                We're awaiting the starting gun..

                ''')
    sh(2)
    for i in range(d(5, 10)):
        print('.')
        sh(1)

    gap(2); print('                        !! Honk !!'); gap(2)
    sh(3)
    print('\nThe stall gates open and the horses are off and racing!')
    sh(2)

    segments = u.laps * 4

    raceroutine(segments)


def sleep():

    sh(2); print('\n sleep time..\n'); sh(1)
    for y in range(d(4, 6)):
        for i in range(d(2, 6)):
            print('.', end="")
        print('...zzZ..'); sh(d(0, 2))
        print('\n' * d(0, 1))

    for flag in u.flags: u.flags[flag] = 0
    u.flags['guide'] = 1
    u.flags['bookie'] = 1

    return game


def track():

    clr()

    if u.betyet == 0:
        print('track details..\n')
        print('    track:', u.weather['dirt'])
        print('    weather:', u.weather['feel'], '&', u.weather['sky'])
        flag('track')  #track now closes until bet made
        if u.laps == 1: laps = 'lap'
        else: laps = 'laps'
        print('\nToday,', u.today +
            ': there will be', u.laps, laps, 'of the track for the race')
        return menu

    race()

    sh(2); print('\n amazing race...'); sh(3)

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
        u.meetnext = []  #make a list of unmet people

        for person in u.meet:
            if u.meet[person][1] == 0:
                u.meetnext.append(person)

    if u.someone == 'May Lee': they = 'She'
    else: they = 'He'

    if u.met == 0:
        they = 'The person'
        someone = 'a person'
    else: someone = u.someone

    if len(u.meetnext) == 0:  #no more unmet peeps, all done
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

    sh(2)
    print('''
You see {0} sitting on a wooden bench.
    {1} gestures. You approach.'''.format(someone, they))
    sh(2)

    if someone == 'a person':
        print("    {} says: I have a clue for you".format(they))
        sh(2)
        print('\n        My name is', u.someone)
        print("    Come see me when you're ready")
        u.bag['clues'] = 1
    else:
        sh(2)
        print('\n    {} asks: '.format(they) +
            'Have you got the answer yet?')

    something = '\nYou keep the clue in your pocket..\n'

        #to do, to do, to do, to dooo, to dooo
    sh(2)
    if d(1, 3) != 3:
        silver = input('\nSolve the clue? y/n -> ')
        if 'y' in silver.lower():
            if d(1, 3) == 1:
                u.clued == 1
                u.clues += 1
                u.met = 0
                u.bag['clues'] = 0
                something = "\nCool bananas!\n"
                sh(1)
                print(clues(u.clues))
                sh(2)
            else:
                print('            no. not this time..')
                sh(2)

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

    if u.money < 1 and u.betyet == 0:
        lucky = d(2, 5)
        print('    You find', lucky, 'dollars.')
        u.money += lucky

    if u.betyet == 0 and u.flags['guide'] == 1:
        sh(1.5)
        print('''

    You find today's newspaper sitting on a wooden bench.
        The story of the criminal underworld war continues...

        There is a racing guide in the paper. You take it.

        ''')

        u.bag['guide'] = 1
        u.flags['guide'] = 0
        u.flags['bookie'] = 0

    if (u.betyet == 1 and u.flags['track'] == 1
        and u.flags['bookie'] == 1):
            something = clue()
            sh(1.5); print(something); sh(3)

    return menu


def odds(horse):

    odds = round((float(u.horses_per) * horse.rank /
                        (u.horses_per - 2) / 6), 3)
    if horse.rank < 4: odds += (d(23, 33) / 100.0)
    elif horse.rank < 7: odds += (d(13, 23) / 100.0)
    horse.odds = odds
    horse.oddstring = str(format(round(odds, 1), '0.2f'))


def lanes():

    u.lanes = {}  #dic of lanenum: horseinstance

    for lane, horsenum in u.racing.items():

        u.lanes[lane] = u.D[horsenum]
        u.lanes[lane].lane = lane
        odds(u.lanes[lane])
        u.lanes[lane].notice = " "

        if u.lanes[lane].stars > 0:
            u.lanes[lane].notice = "* "


def printlanes():

    for lane in u.lanes:

        print('(' + u.lanes[lane].oddstring + ')','Lane %02d' % lane,
            '- Horse %02d -' % u.lanes[lane].number,
            u.lanes[lane].name,
            u.lanes[lane].notice)


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

    u.betyet = 1
    u.flags['track'] = 0
    flag('bookie')
    sh(2)
    print('\n  You no longer need the guide.')
    sh(1.5)
    print('\nYou trash it on the way out of the bookie tent.\n')
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

        if bet == 0: return bookie

        u.ticket[horse] = bet

        u.money -= bet

        print('\n        Ticket:', u.ticket)

        if len(u.ticket) < u.bets and u.money >= 1:
            print('\n    You may bet on another horse')
            a = input('  Enter 1 to bet again.  ')
            if a == '1':
                return bookie(extras=1)

        betdone()

        return menu


def bookie(extras=0):

    clr()

    if u.betyet == 0:

        if extras == 0:
            enter = '\nTalk to bookie. Get scoop. Bet money.. OK?  '
            bookup = input(enter)
            if 'n' in bookup.lower(): return menu

        saymoney()

        print('\n  \\|  Enter lane number to bet on horse  |/\n')

        for lano, horsey in u.lanes.items():
            print(str(lano) + '\t' + horsey.name)

        lane = 23

        while lane - 1 not in range(u.horses_per):
            if lane == 0: break
            try:
                lane = int(input("\ntype 0 to close betting\n"))
                if u.lanes[lane] in u.ticket:
                    print('\n    You have bet on that horse already')
                    print('  Choose another one..\n')
                    print(u.lanes)
                    lane = 23
            except: continue

        if lane != 0:
            return bet(lane)

        if len(u.ticket) == 0: return menu

        print(u.ticket)

        betdone()

        return menu

    else:
        checkit = input('\nCheck winnings. Collect. Ok? ')
        if 'n' in checkit.lower(): return menu
        flag('bookie')

        print('\nYour ticket:',u.ticket)
        winner = u.possy[0]
        winner.wins += 1
        print('\nWinner:', winner)

        if winner in u.ticket.keys():
            print('\nWinner!')
            winnings = round(u.ticket[winner] * winner.odds, 2)
            u.money += winnings
            print('You receive $', winnings + '!')

        else: print('\nBetter luck tomorrow..')


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
        print ('                {} weather.'.format(
                            Horse.weaknesses[horse.weakness]))
    else:
        print ('                {} lanes.'.format(
                            Horse.weaknesses[horse.weakness]))

    print('\nHorse rank:', horse.rank)

    if len(horse.badges) == 0:
        print('\nNo badges')
    else:
        print('Horse stars:', horse.stars)
        for badge in horse.badges: print ('*', badge)

    input('\nOk? ')

    return guide


def chooseHorses(numhorses):

    gamehorses = []

    while len(gamehorses) < numhorses:
        randhorse = choice(Horselist()).strip()
        if randhorse in gamehorses: continue
        gamehorses.append(randhorse)

    return gamehorses


def gameover():

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

    sh(1.5); print()

    for num, door in u.doors.items():

        if door in u.flags and u.flags[door] == 1: continue

        print(' {0} - {1}'.format(num, door))

    while True:

        try:
            path = int(input('\n '))
        except:
            continue

        if path == 1: return bag

        if (path in u.doors and u.doors[path] in u.flags
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

    sh(1)
    return menu


def racing():

    u.racing = {}  #dic of lanenum: horsenum

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
    wannasave = input('\nSaving now, ok?  ')
    if 'n' in wannasave.lower(): return options

    flag('options')

    with open('save.dat', 'wb') as data:
            pickle.dump(u, data)
    message = 'Saved, ' + u.name + '.. Continue game or quit?\n'
    saved = input(message)
    if 'q' in saved.lower(): return gameover

    clr()
    return menu


def load():

    global u

    clr()

    try:
        with open('save.dat', 'rb') as data:
            u = pickle.load(data)
    except:
        print('No load game to load.. Starting new game..')
        sh(3)
        return main(game='new')

    Horse.counter = len(u.gameHorses)
    loaded = 'Loaded.. Welcome back, ' + u.name
    sh(1.5); print(loaded); sh(2.5)

    flag('options')
    clr()
    sh(1)

    for horse in u.D.values():

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
            7 - Gamespeed
            9 - Quit

        ''')

    while True:

        try: i = int(input('\n ? '))
        except: continue

        if i not in [1, 4, 6, 7, 9]: continue
        if i == 9: return gameover
        if i == 6: return save
        if i == 4: return load
        if i == 7:
            if u.wait == 1:
                u.wait = 0.5
                print('        Game now at double speed')
            else: u.wait = 1; print('        Game now at normal speed')
            sh(2); return options

        return menu


def broadcast():

    weekday = u.day % 7
    days = ['Sunday', 'Moonday', 'Marsday', 'Mercuryday',
                'Jupiterday', 'Venusday', 'Saturnday']
    u.today = days[weekday]

    print('        The alarm goes off.', end="")
    sh(2)
    print(' The alarm goes on.'); sh(2)

    print('\nOn comes the morning radio broadcast..\n')

    sh(1); print(u.today); sh(1)

    weather()

    print('\nThe temperature today is',
            u.weather['temp'], 'degrees.')

    sh(1.5)

    print("It's", u.weather['feel'], 'and',
            u.weather['sky'] + '.')

    sh(1); print(); sh(1)

    news()
    racing()
    lanes()

    sh(1); print(); sh(1)

    tis = input("Very interesting, wouldn't you say?\n\n")
    print('\nindeed..', tis)

    sh(2.3)


def game():

    clr()

    u.betyet = 0
    u.ticket = {}

    flag('sleep')
    u.day += 1

    u.laps = d(1, 2)

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


def main(game='load'):

    global u, horse

    clr()

    while True:

        if game == 'new': break

        try:
            print('\n    1 - New game\n    2 - Load')
            hmm = int(input('\n? '))
        except: continue

        if hmm == 2: return load
        if hmm == 1: game = 'new'

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
        u.D[horse.number] = horse  #instance into dictionary

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
