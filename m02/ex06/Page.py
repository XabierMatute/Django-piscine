# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Page.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/21 12:33:03 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/22 11:46:52 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span

class Page:
    def __init__(self, root : Elem):
        self.root = root

    def is_valid(self):
        def validate(elem):
            if isinstance(elem, Text):
                return True
            if elem.tag not in ['html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br']:
                # print(f'Invalid tag: {elem.tag}')
                return False
            if elem.tag == 'html':
                if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
                    # print(f'Invalid html content: {elem.content}')
                    return False
            if elem.tag == 'head':
                if len([e for e in elem.content if isinstance(e, Title)]) != 1:
                    # print(f'Invalid head content: {elem.content}')
                    return False
            if elem.tag in ['body', 'div']:
                if not all(isinstance(e, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for e in elem.content):
                    # print(f'Invalid body content: {elem.content}')
                    return False
            if elem.tag in ['title', 'h1', 'h2', 'li', 'th', 'td']:
                if len(elem.content) != 1 or not isinstance(elem.content[0], Text):
                    # print(f'Invalid {elem.tag} content: {elem.content}')
                    return False
            if elem.tag == 'p':
                if not all(isinstance(e, Text) for e in elem.content):
                    # print(f'Invalid p content: {elem.content}')
                    return False
            if elem.tag == 'span':
                if not all(isinstance(e, (Text, P)) for e in elem.content):
                    # print(f'Invalid span content: {elem.content}')
                    return False
            if elem.tag in ['ul', 'ol']:
                if not elem.content or not all(isinstance(e, Li) for e in elem.content):
                    # print(f'Invalid {elem.tag} content: {elem.content}')
                    return False
            if elem.tag == 'tr':
                ths = [e for e in elem.content if isinstance(e, Th)]
                tds = [e for e in elem.content if isinstance(e, Td)]
                if not elem.content or (ths and tds) or (ths and tds):
                    # print(f'Invalid tr content: {elem.content}')
                    return False
            if elem.tag == 'table':
                if not elem.content or not all(isinstance(e, Tr) for e in elem.content):
                    # print(f'Invalid table content: {elem.content}')
                    return False
            return all(validate(e) for e in elem.content)

        return validate(self.root)


    def __str__(self):
        doctype = '<!DOCTYPE html>\n' if isinstance(self.root, Html) else ''
        return f'{doctype}{self.root}'

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))


def test():
    page = Page(Html([
    Head([Title(Text('"Hello ground!"')), Meta({'charset': 'UTF-8'})]),
    Body([])
    ]))
    if page.is_valid():
        print('\nvalid page (example)')
        print(page)
    
    page = Page(Html([
    Head([Title(Text('"Hello ground!"')), Meta({'charset': 'UTF-8'}), Elem('tortilla de patata')]),
    Body()
    ]))

    if not page.is_valid():
        print('\ninvalid page (invalid tag)')
        print(page)
        print()
    
    page = Page(Html([
    ]))

    if not page.is_valid():
        print('\ninvalid page (no head not body)')
        print(page)
        print

    page = Page(Html([
    Body([])
    ]))

    if not page.is_valid():
        print('\ninvalid page (no head)')
        print(page)
        print()

    page = Page(Html([
    Head([Title(Text('"Hello ground!"')), Meta({'charset': 'UTF-8'})]),
    Head([Title(Text('"Bye ground!"')), Meta({'charset': 'UTF-8'})]),
    Body([])
    ]))

    if not page.is_valid():
        print('\ninvalid page (2 heads)')
        print(page)
        print()

    page = Page(Html([
    Head([]),
    Body([])
    ]))
    if not page.is_valid():
        print('\ninvalid page (no tittle tags)')
        print(page)
        print()

    page = Page(Html([
        Head([Title(Text('"Hello ground!"')), Title(Text('"Hello ground!"')), Meta({'charset': 'UTF-8'})]),
        Body([])
    ]))
    if not page.is_valid():
        print('\ninvalid page (2 tittle tags)')
        print(page)
        print()

    page = Page(Html([
    Head([Title(Text('"Hello ground!"'))]),
    Body([Meta({'charset': 'UTF-8'})])
    ]))

    if not page.is_valid():
        print('\ninvalid page (meta in body)')
        print(page)
        print()

    page = Page(Html([
    Head([Title([Text('"Hello ground!"'), Text('"Helllo!"')])]),
    Body([])
    ]))

    if not page.is_valid():
        print('\ninvalid page (2 texts in title)')
        print(page)
        print()

    page = Page(Html([
    Head([Title(H1(Text('"Hello ground!"')))]),
    Body([])
    ]))

    if not page.is_valid():
        print('\ninvalid page (h1 in title)')
        print(page)
        print()

    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([P(Text('"Not allowed here!"'))])
    ]))

    if not page.is_valid():
        print('\ninvalid page (p in body)')
        print(page)
        print()

    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([P(H1(Text('"Not allowed here!"')))])
    ]))

    if not page.is_valid():
        print('\ninvalid page (h1 in p)')
        print(page)
        print()

    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Span(H1(Text('"Not allowed here!"')))])
    ]))

    if not page.is_valid():
        print('\ninvalid page (h1 in span)')
        print(page)
        print()

    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Ul(H1(Text('"Not allowed here!"')))])
    ]))

    if not page.is_valid():
        print('\ninvalid page (h1 in ul)')
        print(page)
        print()

    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Table([Tr([Th(Text('"Header"')), Td(Text('"Data"'))])])])
    ]))

    if not page.is_valid():
        print('\ninvalid page (mix of th and td in tr)')
        print(page)
        print()

    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Table([H1(Text('"Not allowed here!"'))])])
    ]))

    if not page.is_valid():
        print('\ninvalid page (h1 in table)')
        print(page)
        print()

def main():
    test()
    page = Page(Html([
        Head(Title(Text('"Hello ground!"'))),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img({'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ]))
    print(page)

    if page.is_valid() == False:
        print("this page is invalid")
    page.write_to_file("invalid_page.html")

    valid_page = Page(Html([
        Head([Title(Text('"Hello ground!"')), H1(Text('"Oh no, not again!"')), Img({'src': 'http://i.imgur.com/pfp3T.jpg'})]),
        Body([
        ])
    ]))

    print(valid_page)
    if valid_page.is_valid() == False:
        print("this page is invalid")
    valid_page.write_to_file("valid_page.html")

if __name__ == '__main__':
    main()