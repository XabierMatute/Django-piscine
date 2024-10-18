# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/18 13:50:44 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/18 13:58:29 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
    
    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "coffee"
        self.price = 0.40
    
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"
        self.price = 0.30

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50
    
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"

def main():
    caliente = HotBeverage()
    print(caliente)
    print()
    cafelito = Coffee()
    print(cafelito)
    print()
    t = Tea()
    print(t)
    print()
    chocochocolala = Chocolate()
    print(chocochocolala)
    print()
    monje = Cappuccino()
    print(monje)
    print()



if __name__ == "__main__":
    main()