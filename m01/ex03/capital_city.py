# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/15 11:38:57 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/18 12:07:59 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def get_capital_city(state):
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

    if state in states :
        print(capital_cities[states[state]])
    else:
        print("Unknown state")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_capital_city(sys.argv[1])
