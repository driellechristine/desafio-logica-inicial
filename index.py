nome = 'Charizard'
xp = 400

if xp < 1000:
    nivel = 'Ferro'

if xp >= 1001 <= 2000:
    nivel = 'Bronze'

if xp >= 2001 <= 5000:
    nivel = 'Prata'

if xp >= 6001 <= 7000:
    nivel = 'Ouro'

if xp >= 7001 <= 8000:
    nivel = 'Platina'

if xp >= 8001 <= 9000:
    nivel = 'Ascendente'

if xp >= 9001 <= 10000:
    nivel = 'Mortal'

if xp >= 10001:
    nivel = 'Radiante'

print(f'O Herói de nome {nome} está no nivel de {nivel}')
