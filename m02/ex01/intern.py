# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/18 13:44:18 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/18 13:49:10 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return Coffee()


def main():
    intern = Intern()

    mark = Intern("Mark")

    print(f"Intern 1: {intern}")
    print(f"Intern 2: {mark}")

    coffee = mark.make_coffee()
    print(f"Mark's coffee: {coffee}")

    try:
        intern.work()
    except Exception as e:
        print(f"Intern 1 tried to work: {e}")


if __name__ == "__main__":
    main()