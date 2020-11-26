'''
print(1,2,3,sep='\n')

a=list(range(10))
print(a)
b=list(range(5,12))
print(b)
c=list(range(-4,10,2))
print(c)
d=list(range(10,0,-1))
print(d)

a=tuple(range(10))
print(a)

a=[1,2,3]
print(tuple(a))
b=(4,5,6)
print(list(b))

a,b,c=[1,2,3]
print(a,b,c)
d,e,f=(4,5,6)
print(d,e,f)

a=list(range(5,-10,-2))
print(a)

a=[10,20,30,40,50,60,70,80,90]
print(len(a))

print(len(range(0,10,2)))

b=(38,21,53,62,19)
print(b[0])

a=[0,10,20,30,40,50,60,70,80,90]
print(a[2:8:3])

r=range(10)
print(r)
print(r[4:7])
print(r[4:])
print(list(r[:7:2]))

a=[0,10,20,30,40,50,60,70,80,90]
s=slice(4,7)
print(s)
print(a[s])

print(range(10)[slice(4,7,2)])

year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[5:len(year)])
print(population[5:len(population)])
print()
print(year[-3:])
print(population[-3:])

n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

lux = {'health':490,'mana':334,'melee':550,'armor':18.72}
print('lux = ',lux)
lux1 = dict(health=490,mana=334,melee=550,armor=18.72)
print('lux1 = ',lux1)
lux2 = dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
print('lux2 = ',lux2)
print(list(zip([1,2,3],[97,98,99])))
lux3 = dict([('h',490),('mana',334),('melee',550),('armor',18.72)])
print('lux3 = ',lux3)

lux = {'health':490,'mana':334,'melee':550,'armor':18.72}
print(lux['health'])
print(lux)
lux['health']=2037
lux['mana']=1184
print(lux)
lux['mana_regen']=3.28
print(lux)

lux = {'health':490,'mana':334,'melee':550,'armor':18.72}
print('health' in lux)
print(len(lux))

camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(camille['health'])
print(camille['movement_speed'])
'''
