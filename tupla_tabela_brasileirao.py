times = ('Corinthians', 'São paulo', 'Palmeiras', 'Santos', 'RedBull',
         'Ceará', 'Fortaleza', 'Gremio', 'Chapecoense', 'Sport',
         'Athletico paranaense', 'Internacional', 'Vasco', 'Goiás', 'Bahia',
         'Flamengo', 'Botafogo', 'Atlético goianiense', 'Atlético mineiro', 'Coritiba')
#for t in times:
    #print(t)
print(f'Os cinco primeiros colocados são: {times[:5]}')
print(f'Os últimos quatro colocados são: {times[-4:]}')
print(sorted(times))
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição.')
