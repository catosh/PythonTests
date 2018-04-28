import os
import json
from collections import Counter

path = '/home/phate/Programming/python/IGData/catoso_20180428'
fname = 'likes.json'
data = json.load(open(os.path.join(path, fname)))
users={}
for elem in data['media_likes']:
    userLike = elem[1]
    if userLike in users:
        users[userLike] += 1
    else:
        users[userLike] = 1
totalLikes = 0
for elem in users:
    totalLikes +=users[elem]
print("Total likes ", totalLikes)

stat = Counter(users)
stat.most_common()
for k, v in stat.most_common(20):
    print('%s: %i' % (k, v))
