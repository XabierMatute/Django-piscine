# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/15 12:21:15 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/15 13:04:29 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def print_info(expresion):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    #asuming that all City and State names are capitalized in the dictionary

    if expresion.title() in states:
        print(f"{capital_cities[states[expresion.title()]]} is the capital of {expresion.title()}", end="\r\n")
        return
    if expresion.title() in capital_cities.values():
        for state, capital in capital_cities.items():
            if capital == expresion.title():
                st = state
                for state, code in states.items():
                    if code == st:
                        print(f"{expresion.title()} is the capital of {state}", end="\r\n")
                        return
    print(f"{expresion} is neither a capital city nor a state", end="\r\n")

def parse_input(input):
    for expresion in input.split(','):
        if expresion.strip():
            print_info(expresion.strip())
            
if __name__ == "__main__":
    if len(sys.argv) == 2:
        parse_input(sys.argv[1])
