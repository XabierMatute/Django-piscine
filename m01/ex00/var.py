# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/14 20:22:42 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/18 12:03:20 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_varinfo(variable):
    print(f"{variable} has a type {type(variable)}")

def my_var():
    integer = 42
    print_varinfo(integer)

    string = "42"
    print_varinfo(string)

    jeje = "quarante-deux"
    print_varinfo(jeje)

    floatingpoint = 42.
    print_varinfo(floatingpoint)

    booleano = True
    print_varinfo(booleano)

    lista = [42]
    print_varinfo(lista)

    rae = {42: 42}
    print_varinfo(rae)

    tupleware = (42,)
    print_varinfo(tupleware)

    seta = set()
    print_varinfo(seta)
    
    

if __name__ == '__main__':
    my_var()