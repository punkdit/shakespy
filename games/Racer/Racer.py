#! /usr/bin/python3

from __future__ import print_function
from time import sleep as pause
from random import choice, randint as d
from Racer_data import *
import pickle


Heart = True


class U(object):

    def __init__(self, name):

        self.D = {}
        self.name = name
        self.wait = 1  #0.1 #weeeeeee!
        self.bets = 2
        self.money = 23.0
        self.day = 0
        self.betyet = 0
        self.clued = 0
        self.clues = 0
        self.met = 0
        self.bye = 0
        self.next = 0
        self.checker = 0
        self.end = 0
        self.races = 3
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
                        5: ['Chang', 0]}  #, 6: ['Charlie', 0]}
        self.bag = {
                        'pillow': 1, 'comb': 1}
        self.loadnum = 0


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
            if self.speed >= 123:
                if self.wins > 0:
                    self.Star('Rocket')
                if self.strength < 100:
                    self.strength += 1

        if value in ['str', 'strength', 'both']:
            self.strength += amount
            if self.strength >= 132:
                if self.wins > 0:
                    self.Star('Rock')
                if self.speed < 100:
                    self.speed += 1

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
    pause(secs)


def bag():

    clr()
    print("\n        You own..\n")

    for k, v in u.bag.items():
        if v < 1: continue
        if v == 1: v = " "
        else: v = "(" + str(v) + ")"
        print('                ', k, v)
    print('                                ', 'and $' + str(
                                        format(u.money, '0.2f')), 'cash')
    return menu


def flag(flag):  #hide from menu

    u.flags[flag] = 1

    day = 'done'  #maybe.. let's check..

    for v in u.flags.values():
        if v == 0:
            day = 'notdone'
            u.flags['sleep'] = 1
            break

    if day == 'done':
        u.flags['sleep'] = 0  #time for bed


def switch():

    h = u.horses_per - 1
    i = h // 4

    while True:
        x = d(0, h)
        y = d(0, h)
        if x == y or i < (x - y) or i < (y - x): continue
        break

    u.possy[x], u.possy[y] = u.possy[y], u.possy[x]


def possy(horses, halt=0):

    if u.seggy == 1:

        sortpossy = {}
        u.possy = []
        oddslist = []

        for horse in horses:

            oddmeter = horse.odds

            while True:
                if oddmeter in sortpossy:
                    if d(1, 3) != 1:
                        oddmeter += 0.001
                    else: oddmeter -= 0.001
                else: break

            sortpossy[oddmeter] = horse

        for each in sortpossy.keys():
            oddslist.append(each)

        oddslist.sort()

        for oddz in oddslist:
            u.possy.append(sortpossy[oddz])

        switch()
        sh(2)
        gap(3)

        print(); sh(1.5); print()
        print('\n     The horses shake their legs..')
        sh(1.5)
        print('         and begin their equine dance')
        sh(1.5)
        print('             across this', u.weather['dirt'], 'track..\n\n')
        #print('on this', u.weather['feel'], u.today, 'afternoon')
        sh(2.3)
        clr()
        print('Out of the gate..')
        sh(2.3)

    else:

        shuffler = {}

        for lane, horse in u.lanes.items():

            points = horse.trackpoints * 0.23
            strength = horse.strength
            speed = horse.speed

            if (u.horses_per - lane < 2 and horse.weakness == 4) \
            or (lane < 3 and horse.weakness == 3):
                if d(0, 1) == 1:
                    horse.Rise('speed', 0 - d(2, 4))
                else: horse.Rise('speed', d(-2, 0))

            elif horse.weakness == 1 and u.weather['temp'] > 33:
                if d(0, 1) == 1:
                    horse.Rise('str', 0 - d(2, 4))
                else: horse.Rise('both', d(-2, 0))

            elif horse.weakness == 1 and u.weather['temp'] > 26:
                if d(0, 1) == 1:
                    horse.Rise('both', 0 - d(1, 2))
                else: horse.Rise('both', d(0, 1))

            elif horse.weakness == 2 and u.weather['dirt'] == 'damp':
                if d(0, 1) == 1:
                    horse.Rise('speed', 0 - d(1, 2))
                else: horse.Rise('str', d(1, 2))

            elif horse.weakness == 2 and u.weather['dirt'] == 'muddy':
                if d(0, 1) == 1:
                    horse.Rise('speed', 0 - d(2, 3))
                else: horse.Rise('str', d(1, 2))

# weaknesses ^

            if (u.horses_per - lane < 2 and horse.secret == 4) \
            or (lane < 3 and horse.secret == 1):
                if d(0, 1) == 1:
                    horse.Rise('speed', d(1, 3))
                else: horse.Rise('speed', d(0, 1))

            elif horse.secret == 3 and u.weather['temp'] > 33:
                if d(0, 1) == 1:
                    horse.Rise('both', d(1, 2))
                else: horse.Rise('str', d(1, 2))

            elif horse.secret == 3 and u.weather['temp'] > 26:
                if d(0, 1) == 1:
                    horse.Rise('str', d(1, 2))
                else: horse.Rise('both', d(0, 1))

            elif horse.secret == 4 and u.weather['dirt'] == 'damp':
                if d(0, 1) == 1:
                    horse.Rise('str', 1)
                else: horse.Rise('speed', 1)

            elif horse.secret == 4 and u.weather['dirt'] == 'muddy':
                if d(0, 1) == 1:
                    horse.Rise('str', 2)
                else: horse.Rise('both', 1)

# strengths ^

            if u.seggy > 5 and horse.strength > 90:
                horse.Rise('speed', d(2, 3))
                horse.Rise('str', -1)

            elif u.seggy > 4 and horse.strength > 80:
                horse.Rise('speed', d(1, 2))

            if horse.strength < 70 and horse.speed > 70:
                horse.Rise('str', d(1, 2))
                horse.Rise('speed', d(-1, 0))

            if horse.speed < 70 and horse.strength > 70:
                horse.Rise('speed', d(1, 2))
                horse.Rise('str', d(-1, 0))

            if u.seggy > 6 and horse.strength > 75 and horse.speed < 75:
                horse.speed += horse.speed * 0.023

            horse.strength += horse.strength * 0.023

            horse.trackpoints += (horse.strength - strength)
            horse.trackpoints += (horse.speed - speed)

            points += horse.trackpoints * 0.23

            while True:
                if points in shuffler:
                    if d(0, 2) != 1:
                        points += 0.01
                    else:
                        points -= 0.01
                else: break

            shuffler[points] = horse

        u.possy = []
        pointlist = []

        for each in shuffler.keys():
            pointlist.append(each)

        pointlist.sort()
        pointlist.reverse()

        for each in pointlist:
                u.possy.append(shuffler[each])

        switch()

        if halt == 0:
            diffs(horses)


def diffs(oldpossy):

    u.diffs = {}

    for pos, it in enumerate(u.possy):
        if it != oldpossy[pos]:
            u.diffs[it] = oldpossy.index(it) - pos

    for k, v in u.diffs.items():
        updown(k, v)

    print(); sh(1.5); print()
    for booger, horsey in enumerate(u.possy):
        print(str(booger + 1) + ':', horsey, end=" ")
        if horsey in u.ticket:
            print(' <-- your horse')
        else: print(' ')
    sh(1); print()
    print(); sh(2.3); print()


def startnhalf():

    if u.seggy == 5:
        clr()
        print('\nat the halfway mark now..')
        sh(2)

    for i, start in enumerate(u.possy):
        if i == 0:
            slip = d(1, 3)
            if slip == 1:
                if u.seggy == 1:
                    print('\n  ', start, 'has a tops start..')
                else:
                    print('\n  ', start, 'is in the lead..')
            elif slip == 2:
                if u.seggy == 1:
                    print('\n  ', start, 'has an ace start..')
                else:
                    print('\n  ', start, 'is leading the pack..')
            else:
                print('\n  out in front it\'s', start)
        elif i == 1:
            slop = d(1, 3)
            if slop == 1:
                print('just followed by', start)
            elif slop == 1:
                print('in second place it\'s', start)
            else:
                print(start, 'is just behind in second')
        elif i == 2:
            print('  and', start)
        elif start == u.possy[-1]:
            slap = d(1, 3)
            if slap == 1:
                print('   and it\'s', start, 'in last place')
            elif slap == 2:
                print('   and in last.. it\'s', start)
            else:
                print('   with', start, 'in the rear')
        else:
            if d(1, 2) == 1:
                print(' followed by', start)
            else:
                print(' then it\'s', start)
        sh(1.8)

    sh(2.5); gap(3)


def raceroutine(segments):

    for segment in range(segments):
        u.seggy = segment + 1

        clr()

        if u.seggy == segments:
            segger = 'last'

        else:
            segs = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth',
                    5: 'fifth', 6: 'sixth', 7: 'seventh'}
            segger = segs[u.seggy]

        if segger == 'first':
            possy(u.lanes.values())
            startnhalf()

        elif u.seggy == segments:
            possy(u.possy, halt=1)

        else:
            if u.seggy == 5:
                startnhalf()
            else:
                possy(u.possy, halt=0)

        if u.seggy <= segments:
            print('\n    Into the', segger, 'turn..')
            sh(1)
            print(' ~-------------------------~\n')
            sh(2)

        if u.seggy == segments - 1:
            clr()
            possy(u.possy, halt=0)

        if segger == 'last':
            possy(u.possy, halt=1)
            clr()
            print('\nOh ho ho..')
            print('  The final leg..')
            print(); sh(1.5)
            print('\nIn front is', u.possy[0])
            sh(1)
            print('\n     In second it\'s', u.possy[1])
            sh(1)
            print('\n          In third is', u.possy[2])
            sh(2.3)  #; print(); sh(2)
            possy(u.possy, halt=1)
            clr()
            print('\nComing in toward the finish line..')
            sh(1.5)
            print("\n   it's {}..".format(u.possy[0])); sh(1.2)
            print("\n         just in front of {}..".format(u.possy[1]))
            sh(1.2); print('\n     with {} just behind them'.format(u.possy[2]))
            sh(3)
            clr()
            print('\nThe horses pass the post..')
            sh(1)
            print('\nIt\'s all over..')
            sh(2)
            possy(u.possy, halt=1)

            for booger, horsey in enumerate(u.possy):

                horsey.runs += 1

                if booger == 0:
                    print('\n\nWinner is', horsey, end="")
                    print('!\n')
                    sh(3)
                    print('1:', horsey)
                    sh(1)
                else:
                    print(str(booger + 1) + ':', horsey, end=" ")
                    if horsey in u.ticket:
                        print(' <-- your horse')
                    else: print(' ')
                    sh(1)

        gap(2)
        sh(1.5)


def updown(h, v):

    if v == 1 or v == -1: s = 'spot'
    else: s = 'spots'

    if v > 4: m = 'leaps'
    elif v > 2: m = 'jumps'
    elif v < -4: m = 'slides'
    elif v < -2: m = 'slips'
    else: m = 'moves'

    if v < 0:
        a = str(v)[1:]
        c = '\\/'
        t = 'back'
    else:
        a = str(v)
        c = '     /\\'
        t = 'up'

    print(c, h, m, a, s, t)
#'into position', u.possy.index(k) + 1

    sh(1)


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
            horse.Rise('speed', -3)

            if d(0, 1) == 1:
                print('        There is a little delay as',
                        horse, 'resists')
                horse.Rise('both', -2)
                sh(d(3, 5))

        elif horse.weakness == 1 and u.weather['temp'] > 26:
            horse.Rise('both', -3)

            if d(0, 1) == 1:
                print('        There is a little delay..',
                        horse, 'looks a little weak..')
                horse.Rise('both', -2)
                sh(d(3, 5))

        elif horse.weakness == 2 and u.weather['dirt'] == 'wet':
            horse.Rise('str', -3)

            if d(0, 1) == 1:
                print('        There is a little delay..',
                        horse, 'is taking its time..')
                horse.Rise('both', -2)
                sh(d(3, 5))

    sh(3)
    clr()
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
    clr()
    print('\nThe stall gates open and the horses are off and racing!')
    sh(3)

    segments = u.laps * 4

    raceroutine(segments)


def sleep():

    sh(2); print('\n sleep time..\n'); sh(1)
    for y in range(d(6, 9)):
        for i in range(d(2, 7)):
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
        print('\ntoday,', u.today.lower() +
            ': there will be', u.laps, laps, 'of the track for the race')
        return menu

    race()

    sh(2); print('\n amazing race...'); sh(3)
    u.flags['bookie'] = 0  #bookie opens again
    flag('track')  #after race, track closes access for the day

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

    if u.next > 2:

        if u.end < 3:
            flag('garden')
            something = sumting(something)
            return something

        elif u.money < 2350:
                    flag('garden')
                    u.end = 2
                    u.next = 2
                    return something
        else:
            u.bye = 1
            something = ('\nThere is a limo standing by the ' +
            ' the garden entrance.\n  The passenger window ' +
            'slides down.\n   May Lee gestures.\n\n"It is time.\n')
            return something

    if u.met == 0 and len(u.meetnext) == 0:  #no more unmet peeps, all done
        u.clued == 2
        u.met = 2
        flag('options')
        flag('garden')
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
        print('\n              My name is', u.someone)
        print("            Come see me when you're ready")
        u.bag['clues'] = 1
    else:
        sh(2)
        print('\n     {} asks: '.format(they) +
                    'Have you got the answer yet?')

    something = '\nYou keep the clue in your pocket..\n'

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

    sh(2.3)

    if u.money < 4 and u.betyet == 0:
        sh(1.5)
        lucky = d(1, 10)
        if lucky == 1:
            print('    You find a dollar.')
        else:
            print('    You find', lucky, 'dollars.')
        u.money += lucky
        sh(1.5)
        saymoney()
        sh(1.5)

    if u.betyet == 0 and u.flags['guide'] == 1 and u.bye != 1:
        sh(2.3)
        print('''

    You find today's newspaper sitting on a wooden bench.
        The story of the criminal underworld war continues...

        There is a racing guide in the paper. You take it.

        ''')

        u.bag['guide'] = 1

        u.flags['guide'] = 0  #guide available
        u.flags['bookie'] = 0  #bookie open
        sh(2)

    if u.met == 2 and u.bye != 1:
        if u.next > 2:
            something = clue()
            sh(1.5); print(something); sh(3)
        else:
            print('\n  You feel a presence here.'); sh(1.5)
            print(choice(['  .. there is a sweet flower smell ..\n',
                        ' .. you sense a warmth nearby ..\n',
                        ' .. you feel a shiver, your hairs bristle ..\n']))
            u.next += 1
        flag('garden')
        flag('options')

    if (u.betyet == 1 and u.flags['track'] == 1
        and u.flags['bookie'] == 1):
            something = clue()
            sh(1.5); print(something); sh(3)

    if u.bye == 1: return bye

    return menu


def bye():

    input('Ready?\n')
    clr()
    print('\n you think about your life in the gutter..'); sh(1)
    sh(1); print('\n  and these last', u.day, 'days of the groundhog grind..')
    print('\n it\'s time to move on..'); sh(1)
    sh(1); print('   and be..'); sh(3)
    print('\n                    !Happy Happy Ever After!')
    sh(5)
    print('\namazing game...')
    sh(5)
    input('howzat?\n')
    return gameover


def odds(horse):

    odds = horse.rank / 2 + 1.23

    changer = d(-23, 23)
    if changer == 0: changer = 0.01
    else: changer *= 0.007
    changer += 1

    odds *= changer

    horse.odds = odds
    horse.oddstring = str(format(round(odds, 1), '05.2f'))


def lanes():

    u.lanes = {}  #dic of lanenum: horseinstance

    for lane, horsenum in u.racing.items():

        u.lanes[lane] = u.D[horsenum]
        u.lanes[lane].lane = lane  #love that line

        horsi = u.lanes[lane]

        odds(horsi)  #calculate horse odds

        horsi.notice = " "

        if horsi.stars > 0:
            horsi.notice = "* "


def guide():

    clr()
    print(u.today)
    print("\nLet's see who's racing today..\n")
    print(' Lanes  -  Odds  - Horse\n')

    for lane in u.lanes:
        pony = u.lanes[lane]

        print('Lane %02d -' % lane, '[' + pony.oddstring + ']',
                '<' + str(format(pony.number, '02d')) + '>',
                        pony.name, pony.notice)

    lane = 23

    print('\nEnter lane number to view horse details')

    while lane - 1 not in range(u.horses_per):
        if lane == 0: break
        try: lane = int(input('type 0 to close guide\n'))
        except: continue

    if lane != 0:
        return bio(lane)

    clr()
    return menu


def betdone():

    u.betyet = 1
    u.flags['track'] = 0
    flag('bookie')
    sh(1.5)
    print('\n  You no longer need the guide.')
    sh(1.5)
    print('\nYou trash it on the way out of the bookie tent.\n')
    del u.bag['guide']
    flag('guide')
    u.bag['ticket'] = 1


def bet(lane):

    horse = u.lanes[lane]

    while True:

        print('\nYou are betting on %s' % horse.name)

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
                return bookie

        betdone()

        return menu


def bookie():

    clr()

    if u.betyet == 0:

        print('\nInside the small tent you tap start on the betting terminal..')

        saymoney()

        print('\n  \\|  Enter lane number to bet on horse  \n')

        sh(0.23)

        for lano, horsey in u.lanes.items():
            print('   |  ' + str(lano) + '  ' + horsey.name)

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

        flag('bookie')

        print('\nYour ticket:', u.ticket)
        winner = u.possy[0]
        winner.wins += 1
        print('\nWinner:', winner)

        if winner in u.ticket:
            sh(5)
            print('\nWinner!')
            sh(3)
            saymoney()
            sh(3)
            a = u.ticket[winner] * winner.odds
            winnings = round(a, 2)
            u.money += winnings
            print('\nYou receive $' + str(format(winnings, '0.2f')) + '!')
            sh(3)
            saymoney()

        else: sh(2); print('\nBetter luck tomorrow..')

        u.bag['ticket'] = 0

    return menu


def saymoney():

    u.money = round(u.money, 2)
    print ('\nYou have $' + str(format(u.money, '0.2f')))


def sumting(something):

    sh(1.5); print('\n    You have come a long way,', u.name); sh(2)
    print('\nIt is me, May Lee'); sh(1.5)
    print('Come with me,', u.name); sh(1.5)
    print('\n     I will show you'); sh(2)
    gong = input('\n(will you go with May Lee?)\n')
    if 'n' in gong.lower():
        return something
    something = ('\n   Look out for me, ' + u.name +
                    '. I will come for you soon. \n\n' +
                    'You will need about $2350\n  ')
    flag('garden')
    u.next = 2
    u.end += 1
    return something


def bio(lane):

    clr()

    horse = u.lanes[lane]

    print ("Horse number {0}, {1}, doesn't like ".format(
                horse.number, horse.name), end="")

    weakness = Horse.weaknesses[horse.weakness]

    if horse.weakness in [1, 2]:
        print (weakness, 'weather.')
    else:
        print (weakness, 'lanes.')

    print(horse, 'has won', horse.wins, end=" ")
    if horse.wins == 1:
        print('race out of', horse.runs, end=" ")
    else:
        print('races out of', horse.runs, end=" ")
    if horse.runs == 1: print('run')
    else: print('runs')

    print('\nHorse rank:', horse.rank)

    if len(horse.badges) == 0:
        print('\nNo badges')
    else:
        print('\nHorse stars:', horse.stars)
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

             Quit Racer or Start Again



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

        try: path = int(input('\n '))
        except: continue

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

    sh(1.2)
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

    u.loadnum += 1
    saving = u.name + str(u.loadnum) + '.dat'
    with open(saving, 'wb') as data:
        pickle.dump(u, data)

    print('\nGame saved,', u.name + '..')
    sh(0.7)
    print('\nYour Load number is:', u.loadnum)
    sh(3)

    return options


def load():

    global u

    clr()

    name = input('\nEnter your name\n')
    loadnum = input('\nEnter your load number\n')
    loading = name + loadnum + '.dat'

    try:
        with open(loading, 'rb') as data:
            u = pickle.load(data)
    except:
        print('No load game to load..')
        sh(3)

        try:
            if u: return options
        except:
            return main(game='new')

    Horse.counter = len(u.gameHorses)
    loaded = 'Loaded.. Welcome back, ' + u.name
    sh(1.5); print(loaded); sh(3)

    #flag('options')

    clr()
    sh(1)

    for horse in u.D.values():

        print('Importing..')
        print(format(horse.number, '02d'), horse.name)
        print('Star:', horse.rank)
        print('---------------------------------')
        sh(0.23)

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
            3 - Load
            5 - Save
            7 - Speed
            9 - Quit

        ''')

    while True:

        try: i = int(input('\n ? '))
        except: continue

        if i not in [1, 3, 5, 7, 9]: continue
        if i == 9: return gameover
        if i == 5: return save
        if i == 3: return load
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
    for i in range(3):
        sh(0.5); print('.')
    print('numPad games')
    for i in range(3):
        sh(0.5); print('.')
    print('in association with Shakespy')
    for i in range(3):
        sh(0.5); print('.')
    sh(1); print('.')
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

    input('\n Are you ready? \n  ')

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

    while True:

        try: you = input('Enter your name: ').strip()
        except: continue
        if len(you) < 1: continue
        u = U(you)
        break

    Horse.counter = 0

    print('\nMaximize your window\n')

    u.horses_per = 0

    horses_per = 'Horses per race, ' + u.name + '? (enter 6-9) \n '

    while u.horses_per > 9 or u.horses_per < 6:
        try: u.horses_per = int(input(horses_per))
        except: continue

    u.numhorses = u.horses_per * u.races + d(2, 3)
    u.gameHorses = chooseHorses(u.numhorses)

    gap(3)

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
