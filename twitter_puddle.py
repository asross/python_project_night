#              _ _
#             |7 7|_
#    _        |    6|
#   |5|~ ~ ~ _|     |
#   | |~ ~ _|4      |
#  _| |~ _|3        |
# |2  |_|2          |
# |____1____________|
#  0 1 2 3 4 5 6 7 8
#######################

def twitter_puddle(wall):
    total = 0
    for x in range(1, len(wall)-1):
        here = wall[x]

        left = max(wall[:x])
        if left <= here: continue

        right = max(wall[x+1:])
        if right <= here: continue

        total += min(left, right) - here

    return total

assert(twitter_puddle([]) == 0)
assert(twitter_puddle([5]) == 0)
assert(twitter_puddle([5, 5]) == 0)
assert(twitter_puddle([5, 0, 5]) == 5)
assert(twitter_puddle([2, 5, 1, 2, 3, 4, 7, 7, 6]) == 10)
assert(twitter_puddle([2, 5, 1, 2, 3, 4, 7, 7, 6, 8]) == 11)

print 'tests pass'
