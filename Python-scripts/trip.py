print(""" 
Este programa dice a que destino viajaras en base a los dólares que ahorraste durante el año.
Te puede dar 3 opciones en base a 3 rangos de ahorro:
- Menos de $400 USD
- Igual o mayor a $400 USD hasta $799 USD
- Igual o mayor a $800 USD """)

ahorro = int(input('¿Cuanto dinero ahorraste durante el año?: '))
berlin = 800
NewYork = 400
if ahorro >= berlin:
    print('¡Felicidades!, los alemanes te esperan con los tarros llenos de cerveza 🍻 . ¡Iras a Berlin, Alemania 🇩🇪 !')
elif NewYork <= ahorro:
    print('La estátua de la libertad 🗽 te saluda porque a ¡Nueva York es a donde irás 🇺🇸 !')
else:
    print('Bueno, pues prepara los sandwiches 🥪 y lleva repelente para mosquitos 🦟 , porque ¡el parque de la esquina, te espera!')