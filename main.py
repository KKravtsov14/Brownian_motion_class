from classes import Molecule
import turtle as t
import random as r

t.tracer(0)
t.hideturtle()
t.delay(60)

def main():
    '''
    main function
    :return:
    '''
    mol1 = Molecule(r.randint(1, 10), r.randint(0, 10), r.randint(-10, 10), r.randint(-10, 10))
    mol2 = Molecule(r.randint(1, 10), r.randint(0, 10), r.randint(-10, 10), r.randint(-10, 10))
    mol3 = Molecule(r.randint(1, 10), r.randint(0, 10), r.randint(-10, 10), r.randint(-10, 10))
    mol4 = Molecule(r.randint(1, 10), r.randint(0, 10), r.randint(-10, 10), r.randint(-10, 10))
    while True:
        mol1.move()
        mol2.move()
        mol3.move()
        mol4.move()
        t.clear()
        mol1.show()
        t.update()
        mol2.show()
        t.update()
        mol3.show()
        t.update()
        mol4.show()
        t.update()

main()