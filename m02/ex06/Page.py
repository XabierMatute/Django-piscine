# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Page.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/21 12:33:03 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/21 13:40:20 by xmatute-         ###   ########.fr        #
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
                print(f'Invalid tag: {elem.tag}')
                return False
            if elem.tag == 'html':
                if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
                    print(f'Invalid html content: {elem.content}')
                    return False
            if elem.tag == 'head':
                if len([e for e in elem.content if isinstance(e, Title)]) != 1:
                    print(f'Invalid head content: {elem.content}')
                    return False
            if elem.tag in ['body', 'div']:
                if not all(isinstance(e, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for e in elem.content):
                    print(f'Invalid body content: {elem.content}')
                    return False
            if elem.tag in ['title', 'h1', 'h2', 'li', 'th', 'td']:
                if len(elem.content) != 1 or not isinstance(elem.content[0], Text):
                    print(f'Invalid {elem.tag} content: {elem.content}')
                    return False
            if elem.tag == 'p':
                if not all(isinstance(e, Text) for e in elem.content):
                    print(f'Invalid p content: {elem.content}')
                    return False
            if elem.tag == 'span':
                if not all(isinstance(e, (Text, P)) for e in elem.content):
                    print(f'Invalid span content: {elem.content}')
                    return False
            if elem.tag in ['ul', 'ol']:
                if not elem.content or not all(isinstance(e, Li) for e in elem.content):
                    print(f'Invalid {elem.tag} content: {elem.content}')
                    return False
            if elem.tag == 'tr':
                ths = [e for e in elem.content if isinstance(e, Th)]
                tds = [e for e in elem.content if isinstance(e, Td)]
                if not elem.content or (ths and tds) or (ths and tds):
                    print(f'Invalid tr content: {elem.content}')
                    return False
            if elem.tag == 'table':
                if not elem.content or not all(isinstance(e, Tr) for e in elem.content):
                    print(f'Invalid table content: {elem.content}')
                    return False
            return all(validate(e) for e in elem.content)

        return validate(self.root)


    def __str__(self):
        doctype = '<!DOCTYPE html>\n' if isinstance(self.root, Html) else ''
        return f'{doctype}{self.root}'

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

# Tests
def test_page():
    title = Title([Text("My Page")])
    head = Head([title])
    body = Body([H1([Text("Welcome")]), Span([P([Text("This is a paragraph.")]), P([Text("This is another paragraph.")])])])
    html = Html([head, body])
    page = Page(html)
    
    assert page.is_valid() == True
    print(page)

    page.write_to_file("output.html")

def main():
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