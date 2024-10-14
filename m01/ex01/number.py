# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    number.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/14 20:40:56 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/14 20:58:56 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def put_numbers_from_file():
    with open("numbers.txt", "r") as file:
        print("\n".join(file.read().split(',')))

if __name__ == "__main__":
   put_numbers_from_file()
