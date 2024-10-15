# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var_to_dir.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/15 11:24:18 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/15 11:38:03 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def my_first_dic():
    l = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    
    # truple list to dictionary
    d = {year: name for name, year in l}

    # print dictionary
    print("\n".join([f"{year} : {name}" for year, name in d.items()]))


if __name__ == "__main__":
    my_first_dic()
