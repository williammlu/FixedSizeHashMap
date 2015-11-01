from kpcb import *
import time

f = open('hamlet.txt')
words = f.read().split()
kmap = KPCBHashMap(len(words))
print(len(words)," words in file.")



def run():
        (kmap.set(words[count], count ) for count in range(len(words)))

startTime = time.time()

for c in range(100):
        run()
        kmap = KPCBHashMap(len(words)) #clear hashmap
elapsedTime = time.time() - startTime
print('[{}] finished in {} ms'.format('KPCBHashMap', int(elapsedTime * 1000)))
print('It took ', elapsedTime, ' to add hamlet.txt 100 times')

