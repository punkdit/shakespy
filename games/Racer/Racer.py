#!/usr/bin/env python3

'''Racer
(c)2017->
stOneskull'''

import os
import pickle
from time import sleep as pause
from random import randint as d, choice

from horse import Horse
from player import U


__version__ = '0.1.23.3' #shakespy
os.chdir('../games/Racer')


Heart = True


def clr(lines=99):
    '''print new lines'''
    print('\n' * lines)


def sh(secs):
    '''pause by wait'''
    pause(secs * u.wait)


def nature():
    '''temperature and moisture random'''

    temp = d(7, 42)
    rains = d(0, 3)

    if temp < 17: feel = 'cool'
    elif temp > 23: feel = 'warm'
    else: feel = 'mild'

    dirt = ['hard', 'soft', 'damp', 'muddy'][rains]
    sky = ['clear', 'breezy', 'cloudy', 'rainy'][rains]

    return {'temp': temp, 'feel': feel,
            'dirt': dirt, 'sky': sky}


def saybag():
    '''prints out inventory'''

    clr()
    print("\n        You own..\n")

    for thing, amount in u.bag.items():
        if amount < 1: continue
        amount = '' if amount == 1 else f'({amount})'
        print('                ', thing, amount)
    print('                              ',
          f'and ${u.money:.2f} cash')

    return menu


def saymoney():
    '''prints out player wallet value'''

    u.money = round(u.money, 2)
    print('\nYou have $' + str(format(u.money, '0.2f')))


def flag(theflag, hide=1):
    '''hide from menu, 1 is hidden'''

    u.flags[theflag] = hide

    theday = 'done'  # maybe.. let's check..

    for v in u.flags.values():
        if v == 0:
            theday = 'notdone'
            u.flags['sleep'] = 1
            break

    if theday == 'done':
        u.flags['sleep'] = 0  # time for bed


def switch():
    ''' switch two horses next to each other
            can be two spots if 9 racers'''

    h = u.horses_per - 1
    i = h // 4

    while True:
        m = d(0, h)
        a = d(0, h)
        if a == m: continue
        if i < (m - a) or i < (a - m): continue
        break

    u.possy[m], u.possy[a] = u.possy[a], u.possy[m]


def startrace(horses):
    sortpossy = {}
    u.possy = []

    for horse in horses:

        oddmeter = horse.odds

        while oddmeter in sortpossy:
            oddmeter += 0.001

        sortpossy[oddmeter] = horse

    oddslist = sorted(sortpossy)

    u.possy.extend(sortpossy[oddz] for oddz in oddslist)

    switch()
    switch()
    switch()

    sh(2)
    clr(3)

    print()
    sh(1.5)
    print()
    print('A', u.weather['feel'], u.today, 'afternoon at the races!')
    sh(2)
    clr()
    sh(1.5)
    print('\n\n     The horses shake their legs..')
    sh(1.5)
    print('\n         and begin their equine dance')
    sh(1.5)
    print('\n             across the', u.weather['dirt'], 'track..\n\n')

    sh(2.3)
    clr()
    print('Out of the gate..')
    sh(2.3)


def possy(horses, halt=0):
    '''create order of horses in a list,
    halt 1 won't check diffs from last list'''

    if u.seggy == 1:  #  if start of race

        startrace(horses)
    else:
        shuffler = shuffle()

        u.possy = []
        pointlist = sorted(shuffler)
        pointlist.reverse()

        u.possy.extend(shuffler[each] for each in pointlist)

        switch()

        if halt == 0:
            diffs(horses)


def diffs(oldpossy):
    '''working out the difference of horse position
    between race legs for commentating'''

    diffsdict = {
        horse: oldpossy.index(horse) - position
        for position, horse in enumerate(u.possy)
        if horse != oldpossy[position]
    }

    # change is the old position in the possy minus the new position
    # third place to fifth would be change of minus two
    # send diffs to updown func to commentate position changes

    updown(diffsdict)

    # after commenting changes then display all current positions

    print(); sh(1.5); print()
    for position, horsey in enumerate(u.possy):
        print(f'{position + 1}: {horsey}', end=" ")
        print(' <-- your horse') if horsey in u.ticket else print()
    sh(1); print()
    print(); sh(2.3); print()


def bye():
    '''wave'''

    input('Ready?\n')
    clr()
    u.wait = 1
    print('\n you think about your life in the gutter..'); sh(2)
    sh(1); print('\n  and these last', u.day, 'days of the groundhog grind..')
    sh(2); print('\n it\'s time to move on..'); sh(3)
    sh(1); print('\n   and be..'); sh(3)
    print('\n\n              !0! ! !Happy Happy Ever After! ! !0!')
    sh(5)
    print('\n\namazing game...')
    sh(5)
    say = input('\n               howzat?\n        ')
    print('\n\n  indeed..', say)
    sh(2)
    return gameover


def odds(horse):
    '''secret bookie formula'''

    theodds = horse.rank / 2 + 1.23

    changer = d(-23, 23)
    if changer == 0: changer = 0.01
    else: changer *= 0.007
    changer += 1

    theodds *= changer

    horse.odds = theodds
    horse.oddstring = f'{round(theodds, 1):05.2f}'


def startnhalf():
    '''extra commentary at beginning of race
    and halfway if there is a second lap'''

    if u.seggy == 5:
        clr()
        print('\n..at the halfway mark now..')
        sh(2)

    for i, start in enumerate(u.possy):

        if i == 0:
            slip = d(1, 3)
            if slip == 1:
                if u.seggy == 1:
                    print(f'\n   {start} has a tops start..')
                else:
                    print(f'\n   {start} is in the lead..')
            elif slip == 2:
                if u.seggy == 1:
                    print(f'\n   {start} has an ace start..')
                else:
                    print(f'\n   {start} is leading the pack..')
            else:
                print(f"\n  out in front it's {start}")

        elif i == 1:
            slop = d(1, 3)
            if slop == 1: print('just followed by', start)
            elif slop == 3: print('in second place it\'s', start)
            else: print(start, 'is just behind in second')

        elif i == 2:
            if d(1, 2) == 2: print(start, 'in third')
            else: print('  and', start)

        elif start == u.possy[-1]:
            slap = d(1, 3)
            if slap == 1: print('   and it\'s', start, 'in last place')
            elif slap == 3: print('   and in last.. it\'s', start)
            else: print('   with', start, 'in the rear')

        elif d(1, 2) == 1: print(' followed by', start)
        elif d(1, 2) == 1: print(' and then', start)
        else: print(' then it\'s', start)

        sh(1.8)

    sh(2.5); clr(3)


def laneresistance(horse, lane):
    return(
        u.horses_per - lane < 2 and horse.weakness == 4 or
        lane < 3 and horse.weakness == 3
    )


def veryhot(horse):
    return horse.weakness == 1 and u.weather['temp'] > 33


def hot(horse):
    return horse.weakness == 1 and u.weather['temp'] > 26


def shuffle():
    '''monitor conditions through race'''

    shuffler = {}

    for lane, horse in u.lanes.items():

        points = horse.trackpoints * 0.23
        strength = horse.strength
        speed = horse.speed

        if laneresistance(horse, lane):
            if d(0, 1) == 1:
                horse.rise('speed', 0 - d(2, 4))
            else: horse.rise('speed', d(-2, 0))

        elif veryhot(horse):
            if d(0, 1) == 1:
                horse.rise('str', 0 - d(2, 4))
            else: horse.rise('both', d(-2, 0))

        elif hot(horse):
            if d(0, 1) == 1:
                horse.rise('both', 0 - d(1, 2))
            else: horse.rise('both', d(0, 1))

        elif horse.weakness == 2 and u.weather['dirt'] == 'damp':
            if d(0, 1) == 1:
                horse.rise('speed', 0 - d(1, 2))
            else: horse.rise('str', d(0, 1))

        elif horse.weakness == 2 and u.weather['dirt'] == 'muddy':
            if d(0, 1) == 1:
                horse.rise('speed', 0 - d(2, 3))
            else: horse.rise('str', d(0, 1))

# weaknesses ^ ---------- ^

        if (u.horses_per - lane < 2 and horse.secret == 4) \
               or (lane < 3 and horse.secret == 1):
            if d(0, 1) == 1:
                horse.rise('speed', d(0, 2))
            else: horse.rise('speed', d(0, 1))

        elif horse.secret == 1 and u.weather['temp'] > 33:
            if d(0, 1) == 1:
                horse.rise('both', d(0, 1))
            else: horse.rise('str', d(0, 2))

        elif horse.secret == 1 and u.weather['temp'] > 26:
            if d(0, 1) == 1:
                horse.rise('str', d(0, 1))
            else: horse.rise('both', d(0, 1))

        elif horse.secret == 2 and u.weather['dirt'] == 'damp':
            if d(0, 1) == 1:
                horse.rise('str', 1)
            else: horse.rise('speed', 1)

        elif horse.secret == 2 and u.weather['dirt'] == 'muddy':
            if d(0, 1) == 1:
                horse.rise('both', 1)
            else: horse.rise('str', 1)

# strengths ^ ------------ ^

        if u.seggy > 5 and horse.strength > 90:
            horse.rise('speed', 1)
            horse.rise('str', -1)

        elif u.seggy > 4 and horse.strength in range(80, 90):
            horse.rise('speed', 1)

        if horse.strength < 70 and horse.speed > 70:
            horse.rise('str', d(1, 2))
            horse.rise('speed', d(-1, 0))

        if horse.speed < 70 and horse.strength > 70:
            horse.rise('speed', d(1, 2))
            horse.rise('str', d(-2, 0))

        if u.seggy > 6 and horse.strength > 75 and horse.speed < 75:
            horse.speed += horse.speed * 0.023

        horse.strength += horse.strength * 0.023

        horse.trackpoints += (horse.strength - strength)
        horse.trackpoints += (horse.speed - speed)

        points += horse.trackpoints * 0.23

        while points in shuffler:
            if d(0, 1):
                points += 0.01
            else:
                points -= 0.01

        shuffler[points] = horse

    return shuffler


def raceroutine(segments):
    '''take in race legs and direct each leg accordingly'''

    for segment in range(segments):
        u.seggy = segment + 1

        clr()

        if u.seggy == segments:
            segger = 'last'

        else:
            segs = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth',
                    5: 'fifth', 6: 'sixth', 7: 'seventh'}
            segger = segs[u.seggy]

    # check for action depending on segment

        if segger == 'first':
            possy(u.lanes.values())
            startnhalf()

        elif u.seggy == segments:  # if last leg
            possy(u.possy, halt=1)

        elif u.seggy == 5:  # if into a second lap
            startnhalf()

        else:
            possy(u.possy)

        if u.seggy <= segments:
            print(f'\n    Into the {segger} turn..')
            sh(1)
            print(' ~-------------------------~\n')
            sh(2)

        if u.seggy == segments - 1:  # if second last segment
            clr()
            possy(u.possy)

        if segger == 'last':
            possy(u.possy, halt=1)
            clr()
            print('\nOh ho ho..')
            print('  The final leg..')
            print(); sh(2)
            print(f'\nIn front is {u.possy[0]}')
            sh(1)
            print(f"\n     In second it's {u.possy[1]}")
            sh(1)
            print(f'\n          In third is {u.possy[2]}')
            sh(2.3)
            possy(u.possy, halt=1)

            clr()
            print('\nComing in toward the finish line..')
            sh(1.5)
            print(f"\n   it's {u.possy[0]}..")
            sh(1.2)
            print(f"\n         just in front of {u.possy[1]}..")
            sh(1.2)
            print(f'\n     with {u.possy[2]} just behind them')
            sh(3)
            clr()
            print('\nThe horses pass the post..')
            sh(1)
            print('\nIt\'s all over..')
            sh(2)
            possy(u.possy, halt=1)

            for position, horsey in enumerate(u.possy):
                horsey.runs += 1

                if position == 0:
                    print(f'\n\nWinner is {horsey}!\n')
                    sh(3)
                print(f'{position + 1}: {horsey}', end=" ")
                print(' <-- your horse') if horsey in u.ticket else print()
                sh(1)

        clr(2)
        sh(1.5)


def updown(diffsdict):
    '''horse and the position changed put into the commentary'''

    for h, v in diffsdict.items():
        s = 'spot' if v in (-1, 1) else 'spots'

        if v > 4: m = 'leaps'
        elif v > 2: m = 'jumps'
        elif v < -4: m = 'slides'
        elif v < -2: m = 'slips'
        else: m = 'moves'

        e = u.possy.index(h) + 1
        if e < 4:
            if e == 1: r = 'into first'
            if e == 2: r = 'into second'
            if e == 3: r = 'into third'
        elif u.possy[-1] == h:
            r = 'into last'
        else: r = '..'

        if v < 0:
            a = str(v)[1:]
            c = '     \\/'
            t = 'back'
        else:
            a = str(v)
            c = '/\\'
            t = 'up'

        print(c, h, m, a, s, t, r)

        sh(1.4)


def hothorse(horse):
    horse.rise('both', -3)

    if d(0, 1) == 1:
        print('        There is a little delay..',
                horse, 'looks a little weak..')
        horse.rise('both', -2)
        sh(d(3, 5))


def resistance(horse):
    horse.rise('speed', -3)

    if d(0, 1) == 1:
        print('        There is a little delay as',
                horse, 'resists')
        horse.rise('both', -2)
        sh(d(3, 5))


def race():
    '''at the track and the race is about to begin'''

    clr()

    print(f'On this {u.weather["feel"]}, {u.weather["sky"]} {u.today}...')
    print(f'We have {u.horses_per} racers.')

    for horse, thebet in u.ticket.items():
        money = 'bucks'
        if thebet == 1: money = 'dollar'
        print(f'\nYou have {thebet} {money} bet on {horse}')

    input('\nReady? \n')

    clr()

    sh(2)
    print('    The horses are led into their stalls.')
    sh(3)

# weaknesses.. 1 - hot, 2 - wet, 3 - inside, 4 - outside

    for lane, horse in u.lanes.items():

        print(f'\n  {horse} enters stall {lane}')
        sh(1.5)

        if (u.horses_per - lane < 2 and horse.weakness == 4) \
           or (lane < 3 and horse.weakness == 3):
            resistance(horse)

        elif horse.weakness == 1 and u.weather['temp'] > 26:
            hothorse(horse)


        elif horse.weakness == 2 and u.weather['dirt'] == 'wet':
            horse.rise('str', -3)

            if d(0, 1) == 1:
                print('        There is a little delay..',
                      horse, 'is taking its time..')
                horse.rise('both', -2)
                sh(d(3, 5))

    sh(3)
    clr()
    print('''

                The horses are in the blocks..

                We're awaiting the starting gun..

                ''')
    sh(2)

    for _ in range(d(5, 10)):
        print('.')
        sh(1)

    clr(2); print('                        !! Honk !!'); clr(2)
    sh(3)
    clr()
    print('\nThe stall gates open and the horses are off and racing!')
    sh(3)

    segments = u.laps * 4

    raceroutine(segments)


def sleep():
    '''zzZ'''

    sh(2); print('\n sleep time..\n'); sh(1)
    for _z in range(d(6, 9)):
        for _zz in range(d(2, 7)):
            print('.', end="")
        print('...zzZ..'); sh(d(0, 2))
        print('\n' * d(0, 1))

    for theflag in u.flags: u.flags[theflag] = 0
    flag('guide')
    flag('bookie')

    return game


def track():
    '''if no bets: show info about track
        otherwise: race()!'''

    clr()

    if u.betyet == 0:
        print('track details..\n')
        print('    track:', u.weather['dirt'])
        print('    weather:', u.weather['feel'], '&', u.weather['sky'])
        flag('track')  # track now closes until bet made
        laps = 'lap' if u.laps == 1 else 'laps'
        print(f'\ntoday, {u.today.lower()}:')
        print(f'there will be {u.laps} {laps} of the track for the race')
        return menu

    race()

    sh(2); print('\n amazing race...'); sh(3)
    u.flags['bookie'] = 0  # bookie opens again
    flag('track')  # after race, track closes access for the day

    return menu


def clues(five):
    '''fivespys'''
    letter = 'tad'
    word = f'{letter}.'
    word += letter
    word = word[::-1]
    wordtoyomama = 'word'
    spy = get(word)
    return spy[five]


def clue():
    '''garden adventures'''

    something = ("\nDid you know it's already " +
                 "into the 26th century in Buddhism?\n")

    if u.clued == 1:
        u.clued = 0
        u.met = 0

    if u.met == 0:
        u.meetnext = [person for person in u.meet if u.meet[person][1] == 0]
        they = 'The person'
        someone = 'a person'
    else:
        someone = u.someone
        they = 'She' if someone == 'May Lee' else 'He'

    if u.nexts > 2:

        if u.ends < 3:
            flag('garden')
            return sumting(something)

        elif u.money < 2350:
            flag('garden')
            u.ends = 2
            u.nexts = 2
            return something

        u.bye = 1
        return ('\nThere is a limo standing by the garden entrance.' +
            '\nThe passenger window slides down' + '\nMay Lee gestures'
            + '\nIt is time.')

    if not u.meetnext and u.met == 0:  # no more unmet peeps, all done
        u.clued = 2
        u.met = 2
        flag('options')
        flag('garden')
        return something
    elif u.met == 0:
        meeter = choice(u.meetnext)
        u.meetnext.remove(meeter)
        u.meet[meeter][1] = 1
        u.someone = u.meet[meeter][0]
        u.met = 1

    sh(2)
    print(f'''
    You see {someone} sitting on a wooden bench.
         {they} gestures. You approach.''')
    sh(2)

    if someone == 'a person':
        sayhi(they)
    else:
        sh(2)
        print(f'''\n     {they} asks: 
              Have you got the answer yet?''')

    something = '\nYou keep the clue in your pocket..\n'

    sh(2)

    if d(1, 3) != 3:
        silver = input('\nSolve the clue? y/n -> ')
        if 'n' not in silver.lower():
            if d(1, 3) == 1:
                something = gotcha()
            else:
                print('            no. not this time..')
            sh(2)

    flag('options')
    flag('garden')
    return something


def gotcha():
    u.clued = 1
    u.clues += 1
    u.met = 0
    u.bag['clues'] = 0
    sh(1)
    print(clues(u.clues))
    return "\nCool bananas!\n"


def sayhi(they):
    print(f"    {they} says: I have a clue for you")
    sh(2)
    print(f'\n              My name is {u.someone}')
    sh(1.5)
    print("            Come see me when you're ready")
    u.bag['clues'] = 1


def garden():
    '''a little place to get away'''

    clr()
    print('''

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

        u.flags['guide'] = 0  # guide available
        u.flags['bookie'] = 0  # bookie open
        sh(2)

    if u.met == 2 and u.bye != 1:
        if u.nexts > 2:
            something = clue()
            sh(1.5)
            for line in something.splitlines():
                sh(1.5)
                print('\n'+line)
            sh(3)
        else:
            print('\n  You feel a presence here.'); sh(1.5)
            print(choice(['  .. there is a sweet flower smell ..\n',
                          ' .. you sense a warmth nearby ..\n',
                          ' .. you feel a shiver, your hairs bristle ..\n']))
            u.nexts += 1
        flag('garden')
        flag('options')

    if (u.betyet == 1 and u.flags['track'] == 1
            and u.flags['bookie'] == 1):
        something = clue()
        sh(1.5); print(something); sh(3)

    return bye if u.bye == 1 else menu


def guide():
    '''show list of horses and their odds
        on picking a horse, show bio about horse'''

    clr()
    print(u.today)
    print("\nLet's see who's racing today..\n")
    print(' Lanes  -  Odds  - Horse\n')

    for lane in u.lanes:
        pony = u.lanes[lane]

        theodds = pony.oddstring
        ponynum = f'{pony.number:02d}'
        name = pony.name
        note = pony.notice

        print(
            f'Lane {lane:02d} - [{theodds}] <{ponynum}> {name} {note}'
        )

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
    '''finished with bookie, track opens, get a ticket'''

    u.betyet = 1
    u.flags['track'] = 0
    flag('bookie')
    sh(1.5)
    print('\n  You no longer need the guide.')
    sh(1.5)
    print('\n  You trash it on the way out of the bookie tent.\n')
    del u.bag['guide']
    flag('guide')
    u.bag['ticket'] = 1


def bet(lane):
    '''at the bookie, making a bet'''

    horse = u.lanes[lane]

    while True:

        print('\nYou are betting on %s' % horse)
        print('Enter 0 to cancel bet')
        saymoney()

        try:
            thebet = int(input('\nHow much to bet? '))
        except Exception:
            print('''
                We cannot accept cents for bets.
                We apologise for the inconvenience.
                Only whole numbers please.
                        ''')
            continue

        if thebet > u.money:
            print("\n    You don't have enough money")
            continue

        if thebet < 0:
            print("\n    That doesn't work")
            continue

        if thebet == 0: return bookie

        u.ticket[horse] = thebet

        u.money -= thebet

        print('\n        Ticket:', u.ticket)

        if len(u.ticket) < u.bets and u.money >= 1:
            print('\n    You may bet on another horse')
            a = input('  Enter 1 to bet again.  ')
            if a == '1':
                return bookie

        betdone()

        return menu


def checkticket():
    flag('bookie')

    print('\nYour ticket:', u.ticket)
    winner = u.possy[0]
    winner.wins += 1
    print('\nWinner:', winner)

    if winner in u.ticket:
        uwin(winner)
    else: sh(2); print('\nBetter luck tomorrow..')

    u.bag['ticket'] = 0


def uwin(winner):
    sh(5)
    print('\n !! ! !! ! Winner ! !! ! !!')
    sh(3)
    saymoney()
    sh(3)
    a = u.ticket[winner] * winner.odds
    winnings = round(a, 2)
    u.money += winnings
    print(f'\nYou receive ${winnings:0.2f}!')
    sh(3)
    saymoney()


def bookiebet():
    print('\nInside the small tent you tap start on the betting terminal..')

    saymoney()

    print('\n  \\|  Enter lane number to bet on horse  \n')

    sh(0.23)

    for lano, horsey in u.lanes.items():
        print(f'   |  {lano}  {horsey}')

    lane = 23

    while lane - 1 not in range(u.horses_per) and lane != 0:
        try:
            lane = int(input("\ntype 0 to close betting\n"))
            if u.lanes[lane] in u.ticket:
                print('\n    You have bet on that horse already')
                print('  Choose another one..\n')
                print(u.lanes)
                lane = 23
        except Exception:
            continue

    if lane != 0:
        return bet(lane)

    if not u.ticket: return menu

    print(u.ticket)

    betdone()

    return menu


def bookie():
    '''betting before race, check ticket after race'''

    clr()

    if u.betyet == 0:
        return bookiebet()
    else:
        checkticket()
    return menu


def sumting(something):
    '''lidda bidda sumpin sumpin'''

    sh(1.5); print('\n    You have come a long way,', u); sh(2)
    print('\nIt is me, May Lee'); sh(1.5)
    print('Come with me,', u); sh(1.5)
    print('\n     I will show you'); sh(2)
    gong = input('\n(will you go with May Lee?)\n')
    if 'n' in gong.lower():
        return something

    something = ('\nMuch good. Time for prepare.' +
                 '\n   Look out for me, ' + u +
                 '. I will come for you soon. \n\n' +
                 'You will need about $2350\n  ')
    flag('garden')
    u.nexts = 2
    u.ends += 1
    return something


def bio(lane):
    '''individual entries in the guide showing horse info'''

    clr()

    horse = u.lanes[lane]

    print("Horse number {0}, {1}, doesn't like ".format(
        horse.number, horse.name), end="")

    weakness = Horse.weaknesses[horse.weakness]

    if horse.weakness in [1, 2]:
        print(weakness, 'weather.')
    else:
        print(weakness, 'lanes.')

    print(horse, 'has won', horse.wins, end=" ")
    if horse.wins == 1:
        print('race out of', horse.runs, end=" ")
    else:
        print('races out of', horse.runs, end=" ")
    if horse.runs == 1: print('run')
    else: print('runs')

    print('\nHorse rank:', horse.rank)

    if not horse.badges:
        print('\nNo badges')
    else:
        print('\nHorse stars:', horse.stars)
        for badge in horse.badges: print('*', badge)

    input('\nOk? ')

    return guide


def choosehorses(numhorses):
    '''make a list of random horses for the game'''

    print('enter choosehorses')
    gamehorses = []
    file = 'horselist.dat'
    wholelist = get(file)
    print('wholelist got file')
    print(wholelist)

    print(len(gamehorses), numhorses)
    while len(gamehorses) < numhorses:

        randhorse = choice(wholelist).strip()

        if randhorse in gamehorses: quit()

        gamehorses.append(randhorse)

    print('returning gamehorses')
    return gamehorses


def menu():
    '''main menu'''

    sh(1.5); print()

    for num, door in u.doors.items():

        if door in u.flags and u.flags[door] == 1:
            continue

        print(f' {num} - {door}')


    while True:

        try: path = int(input('\n '))
        except: continue

        if path == 1: return saybag

        if (path in u.doors
                and u.doors[path] in u.flags
                and u.flags[u.doors[path]] == 0):
            return eval(u.doors[path])


def gameover():
    '''start again or quit by breaking wonderwall'''

    global Heart

    clr()

    decision = input('''


                 ___ Game Over ___

               Thank you for playing

                Quit or Start Again



                        ''')

    if 'q' in decision.lower():
        Heart = False

    print(); sh(1); print(); sh(2)

    return main


def options():
    '''options menu'''

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

        if i == 9: return gameover
        if i == 5: return save
        if i == 3: return load
        if i == 7:
            if u.wait == 1:
                u.wait = 0.5
                print('        Game now at double speed')
            else:
                u.wait = 1
                print('        Game now at normal speed')
            sh(2); return options
        if i == 1: return menu


def day():
    '''up and at 'em'''

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


def lanes():
    ''' make dict of lane:horse
        give horse.lane attribute
        make the horse odds for bookie
        give horses a guide notice if star'''

    for lane, horsenum in u.racing.items():

        u.lanes[lane] = u.D[horsenum]
        u.lanes[lane].lane = lane  # love dat line

        horsi = u.lanes[lane]
        odds(horsi)  # calculate horse odds

        horsi.notice = " "
        if horsi.stars > 0:
            horsi.notice = "* "


def racing():
    '''horses in today's race
        racing dict made lanenum:horsenum'''

    lane = 0
    u.racing = {}

    while len(u.racing) < u.horses_per:
        roll = d(1, u.numhorses)
        if roll in u.racing.values():
            continue
        lane += 1
        u.racing[lane] = roll


def broadcast():
    '''at the start of each day the radio says the day of the week,
        the temperature and the weather conditions.
        which horses racing and what lanes they're in are decided here'''

    weekday = u.day % 7
    days = ['Sunday', 'Moonday', 'Marsday', 'Mercuryday',
            'Jupiterday', 'Venusday', 'Saturnday']
    u.today = days[weekday]

    print('        The alarm goes off.', end='', flush=True)
    sh(1)
    print(' The alarm goes on.', end='', flush=True)
    sh(2.3)

    print('\n\nOn comes the morning radio broadcast..\n')

    sh(1); print(u.today); sh(1)

    u.weather = nature()

    print('\nThe temperature today is',
          u.weather['temp'], 'degrees.')

    sh(1.5)

    print("It's", u.weather['feel'], 'and',
          u.weather['sky'] + '.')

    sh(1); print(); sh(1)

    print('Newsy newsy newsy news...')

    racing()
    lanes()

    sh(1); print(); sh(1)

    tis = input("Very interesting, wouldn't you say?\n\n")
    print('\nindeed..', tis)

    sh(2.3)


def game():
    '''reset bets, remove sleep from menu, add a day to the counter..'''

    clr()

    u.betyet = 0
    u.ticket = {}

    flag('sleep')
    u.day += 1

    u.laps = d(1, 2)

    broadcast()

    return day


def intro():
    '''welcome to the game'''

    clr()
    for _ in range(3):
        sh(0.5); print('.')
    print('numPad games')
    for _ in range(3):
        sh(0.5); print('.')
    print('in association with Shakespy')
    for _ in range(3):
        sh(0.5); print('.')
    sh(1); print('.')
    clr()

    print('''
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


def setup():
    '''new game.. initialise horses'''

    Horse.counter = 0

    print('\nMaximize your window for Maximum fun\n')

    while u.horses_per < 6 or u.horses_per > 9:
        horses69 = input(
            f'Horses per race, {u.name}? (enter 6-9)\n'
        )

        try: u.horses_per = int(horses69)

        except Exception:
            continue

    u.numhorses = u.horses_per * u.horse_multi + d(2, 3)
    u.gamehorses = choosehorses(u.numhorses)

    clr(3)

    for name in u.gamehorses:

        horse = Horse(name)  # instance creation!
        u.D[horse.number] = horse  # instance into dictionary

        print('Importing..')
        print(f'{horse.number:02d} {horse}')
        print(f'star: {horse.rank}')
        print('---------------------------------')

        if horse.rank == 1:
            horse.star('Golden Champion')
            horse.star('Rank 1')
        elif horse.rank < 6:
            horse.star('Born Champion')
        if horse.rank < 11:
            horse.star('Top Ten Breed')
        sh(0.13)

    sh(2)

    return intro


def save():
    '''make a savegame using u.name and u.loadnum'''

    clr()

    wannasave = input('\nSaving now, ok?  ')
    if 'n' in wannasave.lower(): return options

    u.loadnum += 1

    saving = f'{u.name}{u.loadnum}.save'

    put(u, saving)

    print(f'\nGame saved, {u}..')
    sh(0.7)
    print(f'\nYour Load number is: {u.loadnum}')
    sh(5)

    return options


def put(data, savefile):
    '''pickle the data'''

    with open(savefile, 'wb') as jar:
        pickle.dump(data, jar)


def get(loadfile):
    ''' return the pickled data or return 'nofile' '''
    try:
        with open(loadfile, 'rb') as jar:
            data = pickle.load(jar)
        return data
    except Exception:
        return 'nofile'


def load():
    '''see if there is a loadfile,
        if not go back to options if in a game or start a new game
        if loadfile, then welcome back, print out horses, goto menu'''

    global u

    clr()

    try:
        if u: name = u.name
    except Exception:
        name = input('\nEnter your name\n').strip()

    loadnum = input('\nEnter your load number\n')
    loadfile = name + loadnum + '.save'

    see = get(loadfile)

    if see == 'nofile':
        print('no file to load!')
        pause(3)
        try:
            if u: return options
        except Exception:
            print('starting new game..')
            pause(3)
            return main(thegame='new')

    u = see

    # load success

    Horse.counter = len(u.gamehorses)
    loaded = f'Loaded.. Welcome back {u}.'
    sh(1.5)
    print(loaded)
    sh(3)

    clr()
    sh(1)

    for horse in u.D.values():

        print('Importing..')
        print(f'{horse.number:02d} {horse}')
        print(f'star: {horse.rank}')
        print('---------------------------------')
        sh(0.23)

    sh(2)
    clr()

    return menu


def main(thegame='load'):
    '''check if new game, if so make a player and go to setup
        or try and load a game'''

    global u

    clr()

    while thegame != 'new':

        print('''
              
              1 - New game
              2 - Load

              q - quit

              ''')
        hmm = input('\n? ')
        if hmm == 'q': return quit
        if hmm == '2': return load
        if hmm == '1': thegame = 'new'

    while True:
        you = input('Enter your name: ').strip()
        if not you: continue
        # hi
        u = U(you)
        return setup


def wonderwall(egg):
    '''humpty dumpty loop'''

    while Heart is True:
        egg = egg()


if __name__ == '__main__':
    wonderwall(main)