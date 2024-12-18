# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/15 12:55:33 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/18 12:16:16 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_varinfo(variable):
    print(f"{variable} has a type {type(variable)}")

def get_atomic_number(period, group):
    # energy_levels = [2, 8, 8, 18, 18, 32, 32]
    energy_levels = [2, 10, 18, 36, 54, 86, 118]
    # hidrogen
    if period == 1 and group == 1:
        return 1
    # noble gases
    if group == 18:
        return energy_levels[period - 1]
    if period <= 1:
        return 'x'
    # alkali and alkaline earth metals (s-block)
    if group <= 2:
        return energy_levels[period - 2] + group
    # p-block
    if group >= 13 and group <= 18:
        return energy_levels[period - 1] - (18 - group)
    if period <= 3:
        return 'x'
    # actinides
    if period == 7 and group == 3:
        return 'A'
    # lanthanides
    if period == 6 and group == 3:
        return 'L'
    # transition metals (d-block)
    if group >= 3 and group <= 12:
        return energy_levels[period - 1] - (18 - group)
    


def get_table_data(filename):
    with open(filename, 'r') as file:
        data = file.read().split('\n')
    elements = {}
    for line in data:
        if not line:
            continue
        element = {}
        element_data = line.split('=')
        name = element_data[0].strip()
        properties = element_data[1].split(',')
        element = {'name': name}
        for property in properties:
            key, value = property.split(':')
            element[key.strip()] = value.strip()
        elements[int(element['number'])] = element
    return elements

def generate_element_td(element):
    class_name = 'element'
    return f"""
        <td class = {class_name}>
            <h4>{element['name']}</h4>
            <ul>
                <li>{element['number']}</li>
                <li>{element['small']}</li>
                <li>{element['molar']}</li>
            </ul>
        </td>
    """
        
def generate_unknown_element_td(number):
    return f"""
        <td class = unknown>
            <h4>Unknown Element</h4>
            <ul>
                <li>{number}</li>
            </ul>
        </td>
    """

def generate_html(elements):
    html = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
    <style>
        body {
            font-family: 'Computer Modern', Arial, sans-serif;
            margin: 30px;
            background-color: #808080;
        }
        table {
            width: 99%;
            border-collapse: collapse;
            border-style: solid;
            border-color: #004200;
        }
        th, td {
            text-align: center;
        }
        ul {
            list-style-type: none;
            text-align: left;
        }
        th {
            border: 2px solid #000000;
            padding: 2px;
            background-color: white;
        }
        .element {
            border: 1px solid #003333;
            background-color: lightblue;
        }
        .unknown {
            border: 1px solid #003333;
            background-color: #77ccff;
        }
        .Actinides {
            border: 1px solid #003333;
            background-color: #ffcc00;
        }
        .Lanthanides {
            border: 1px solid #003333;
            background-color: #ccff00;
        }
        
    </style>
    </head>
    <body>

        <h1>The Periodic Table​</h1>
        <table>
        <tr>
        
    """

    html += f"""
            <th></th>
    """

    for group in range(1, 19):
        html += f"""
            <th>Group {group}</th>
        """
    html += """
        </tr>
    """

    for period in range(1, 8):
        html += "<tr>"
        html += f"<th>Period {period}</th>"
        
        for group in range(1, 19):
            if get_atomic_number(period, group) == 'A':
                html += "<td class = Actinides><h4></h4></td>"
                continue
            elif get_atomic_number(period, group) == 'L':
                html += "<td class = Lanthanides><h4></h4></td>"
                continue
            elif get_atomic_number(period, group) == 'x':
                html += "<td></td>"
                continue
            elif get_atomic_number(period, group) == None:
                html += "<td>?</td>"
                continue
            elif get_atomic_number(period, group) in elements:
                html += generate_element_td(elements[get_atomic_number(period, group)])
            elif isinstance(get_atomic_number(period, group), int):
                html += generate_unknown_element_td(get_atomic_number(period, group))            
        html += "</tr>"
    
    html += """
    </table>
    </body>
    </html>
    """
    with open('periodic_table.html', 'w') as file:
        file.write(html)

def generate_periodic_table(filename):
    generate_html(get_table_data(filename))
    

if __name__ == "__main__":
    generate_periodic_table('periodic_table.txt')