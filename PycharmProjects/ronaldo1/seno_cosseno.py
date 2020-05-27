from math import radians, sin, cos, tan
a = float(input('Digite um angulo: '))
seno = sin(radians(a))
print('O angulo de {} tem o SENO de: {:.2f}'.format(a, seno))

cosseno = cos(radians(a))
print('O angulo de {} tem o COSSENO de: {:.2f}'.format(a,cosseno))

tangente = tan(radians(a))
print('O angulo de {} tem a TANGENTE de: {:.2f}'.format(a,tangente))