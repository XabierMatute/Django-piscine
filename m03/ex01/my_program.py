# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_program.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/29 12:45:26 by xmatute-          #+#    #+#              #
#    Updated: 2024/11/06 14:08:03 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from local_lib.path import Path

def main():
    folder = Path("my_folder").mkdir_p()

    file_path = folder / "my_file.txt"
    
    file_path.write_text("Aupa Pallete!")

    print(file_path.read_text())

if __name__ == '__main__':
    main()