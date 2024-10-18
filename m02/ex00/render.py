# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    render.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/18 12:53:52 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/18 13:40:34 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os, re
import settings

def render(template):
    with open(template, 'r') as f:
        content = f.read()
    
    for key, value in vars(settings).items():
        if key.startswith("__"):  # Ignore internal Python variables
            continue
        print(f"Replacing {{{key}}} with {value}")
        content = content.replace(f'{{{key}}}', str(value))
    
    with open(template.replace('.template', '.html'), 'w') as output:
        output.write(content)
    print('File rendered successfully')

def valid_file(file):
    if not file.endswith('.template'):
        print(f"Error: {file} is not a .template file")
        print("File must be a .template file")
        return False
    if not os.path.isfile(file):
        print(f"Error: {file} does not exist")
        return False
    return True

def valid_imput():
    if len(sys.argv) != 2:
        print("Error: invalid number of arguments")
        print("Usage: python render.py <file>.template")
        return False
    if valid_file(sys.argv[1]):
        return True
    return False


def main():
    try:
        if valid_imput():
            render(sys.argv[1])
        else:
            exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()