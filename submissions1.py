import random
import math

def tit_for_whoops(m, t, s):
    if len(t) < 2:
        return 'c'
    else:
        return 'd' if all([x == 'd' for x in t[-2:]]) else 'c'

def growing_distrust(mine, theirs, state):
    # Start with trust.
    if len(mine) == 0:
        state.append(dict(betrayals=0, trust=True))
        return 'c'

    state_info = state[0]

    # If we're trusting and we get betrayed, trust less.
    if state_info['trust'] and theirs[-1] == 'd':
        state_info['trust'] = False
        state_info['betrayals'] += 1

    # Forgive, but don't forget.
    if random.random() < 0.5 ** state_info['betrayals']:
        state_info['trust'] = True

    return 'c' if state_info['trust'] else 'd'
def stubborn_stumbler(m, t, s):
    if not t:
        s.append(dict(last_2=[], last_3=[]))
    if len(t) < 5:
        return 'c'
    else:
        # Records history to state depending if the last two and three
        # plays were equal
        s = s[0]
        if t[-2:].count(t[-1]) == 2:
            s['last_2'].append(t[-1])
        if t[-3:].count(t[-1]) == 3:
            s['last_3'].append(t[-1])
    c_freq = t.count('c')/len(t)
    # Checks if you've consistently defected against me
    opp_def_3 = s['last_3'].count('d') > s['last_3'].count('c')
    opp_def_2 = s['last_2'].count('d') > s['last_2'].count('c')
    # dist func from 0 to 1
    dist = lambda x: 1/(1+math.exp(-5*(x-0.5)))
    # You've wronged me too much
    if opp_def_3 and opp_def_2:
        return 'd'
    # Otherwise, if you're consistently co-operating, co-operate more
    # the less naive you are
    else:
        return 'c' if random.random() > dist(c_freq) - 0.5 else 'd'

def slider(m, t, s):
    z = [[2, 1], [0, 1], [2, 3], [2, 1]]
    if not s:
        s.append(0)
    else:
        s[0] = z[s[0]][t[-1] == 'c']
    x = s[0]
    return 'c' if x < 2 else 'd'

def tit_for_time(mine, theirs, state):
    theirs = theirs[-30:]
    no_rounds = len(theirs)
    return "c" if no_rounds < 5 or random.random() > theirs.count("d") / no_rounds else "d"

def decaying_memory(me, them, state):
    m = 0.95
    lt = len(them)

    if not lt:
        state.append(0.0)
        return 'c'

    # If it's the last round, there is no reason not to defect
    if lt >= 299: return 'd'

    state[0] = state[0] * m + (1.0 if them[-1] == 'c' else -1.0)

    # Use a gaussian distribution to reduce variance when opponent is more consistent
    return 'c' if lt < 5 or random.gauss(0, 0.4) < state[0] / ((1-m**lt)/(1-m)) else 'd'

def jedi2sith(me, them, the_force):
  time=len(them)
  bad_things=them.count('d')
  dark_side=(time+bad_things)/300
  if dark_side>random.random():
    return 'd'
  else:
    return 'c'

def kickback(m, t, s):
  if len(m) < 10:
    return "c"
  td = t.count("d")
  md = m.count("d")
  f = td/(len(t)+1)
  if f < 0.3:
    return "d" if td > md and random.random() < 0.1 else "c"
  return "c" if random.random() > f+2*f*f else "d"

def alternate(m, t, s):
    if(len(m)==0):
        return 'c' if random.random()>.5 else 'd'
    elif(len(m)>290):
        return 'd'
    else:
        return 'd' if m[-1]=='c' else 'c'

def change_of_heart(m, t, s):
    return 'c' if len(t) < 180 else 'd'

def just_noise(m,t,s):
        return 'c' if random.random() > .2 else 'd'

def vengeful(m,t,s):
    return 'd' if 'd' in t else 'c'
