# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/18 14:03:47 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/18 14:25:46 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.served_drinks = 0
        self.max_drinks_before_break = 10
        self.broken = False

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90
        
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.broken = False

    def serve(self, beverage):
        if self.broken:
            raise CoffeeMachine.BrokenMachineException()
        
        self.served_drinks += 1

        if self.served_drinks % self.max_drinks_before_break == 0:
            self.broken = True

        return random.choice([beverage(), CoffeeMachine.EmptyCup()])

def main():
    machine = CoffeeMachine()

    try:
        print(machine.serve(Tea))
        print(machine.serve(Tea))
        print(machine.serve(Tea))
        print(machine.serve(Tea))
        print(machine.serve(Tea))
        print(machine.serve(Tea))
        print(machine.serve(Tea))
        print(machine.serve(Tea))
        print(machine.serve(Chocolate))
        print(machine.serve(Chocolate))
        print(machine.serve(Chocolate))
        print(machine.serve(Chocolate))
        print(machine.serve(Chocolate))
        print(machine.serve(Chocolate))
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
        machine.repair()
        print("Machine repaired.")
    
    print()
    
    try:
        print(machine.serve(Coffee))
        print(machine.serve(Cappuccino))
        print(machine.serve(Tea))
        print(machine.serve(Chocolate))
        print(machine.serve(Coffee))
        print(machine.serve(Coffee))
        print(machine.serve(Coffee))
        print(machine.serve(Cappuccino))
        print(machine.serve(Chocolate))
        print(machine.serve(Coffee))
        print(machine.serve(Tea))
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
    

if __name__ == "__main__":
    main()