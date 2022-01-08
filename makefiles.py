callme='Beimer'

acciones=[
    'crea',
    'borra',
    'renombra',
]

saludos=[
    'hola',
    'eurus',
    'hi'
]

elements=[
    'carpeta',
    'proyecto'
]

entrada=input('Bienvenido a eurus:')

if(entrada in saludos):
    print("Hola "+callme+' que tienes pensado hacer hoy?')

if(entrada in acciones):
    print('')
