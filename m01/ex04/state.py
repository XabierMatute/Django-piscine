# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    state.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/15 11:46:54 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/15 12:21:52 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def get_state(city):
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

    st = None
    for state, capital in capital_cities.items():
        if capital == city:
            st = state
    if not st:
        print("Unknown capital city")
        return
    for state, code in states.items():
        if code == st:
            print(state)
            return
    # print("Unknown capital city")    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_state(sys.argv[1])