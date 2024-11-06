# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    geohashing.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/23 08:17:07 by xmatute-          #+#    #+#              #
#    Updated: 2024/11/04 18:13:51 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, antigravity

def main():
    if len(sys.argv) != 4:
        print("Usage: python geohashing.py <latitude> <longitude> <date>")
        sys.exit(1)
    try:
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), bytes(sys.argv[3], 'utf-8'))
    except ValueError as e:
        print("Invalid arguments: " + str(e))
        print("Usage: python geohashing.py <latitude> <longitude> <date>")
        sys.exit(1)
    except Exception as e:
        print("An error occurred: " + str(e))
        sys.exit(1)


if __name__ == '__main__':
    main()

