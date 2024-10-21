# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    elements.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/21 11:14:11 by xmatute-          #+#    #+#              #
#    Updated: 2024/10/21 12:30:39 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None):
        super().__init__(tag='html', content=content, tag_type='double')

class Head(Elem):
    def __init__(self, content=None):
        super().__init__(tag='head', content=content, tag_type='double')

class Body(Elem):
    def __init__(self, content=None):
        super().__init__(tag='body', content=content, tag_type='double')

class Title(Elem):
    def __init__(self, content=None):
        super().__init__(tag='title', content=content, tag_type='double')

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='meta', attr=attr, tag_type='simple', content=None)

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='img', attr=attr, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None):
        super().__init__(tag='table', content=content, tag_type='double')

class Th(Elem):
    def __init__(self, content=None):
        super().__init__(tag='th', content=content, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None):
        super().__init__(tag='tr', content=content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None):
        super().__init__(tag='td', content=content, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None):
        super().__init__(tag='ul', content=content, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None):
        super().__init__(tag='ol', content=content, tag_type='double')

class Li(Elem):
    def __init__(self, content=None):
        super().__init__(tag='li', content=content, tag_type='double')

class H1(Elem):
    def __init__(self, content=None):
        super().__init__(tag='h1', content=content, tag_type='double')

class H2(Elem):
    def __init__(self, content=None):
        super().__init__(tag='h2', content=content, tag_type='double')

class P(Elem):
    def __init__(self, content=None):
        super().__init__(tag='p', content=content, tag_type='double')

class Div(Elem):
    def __init__(self, content=None):
        super().__init__(tag='div', content=content, tag_type='double')

class Span(Elem):
    def __init__(self, content=None):
        super().__init__(tag='span', content=content, tag_type='double')

class Hr(Elem):
    def __init__(self):
        super().__init__(tag='hr', tag_type='simple')

class Br(Elem):
    def __init__(self):
        super().__init__(tag='br', tag_type='simple')




def basic_test():
    # Test 1: Html element
    html = Html()
    assert str(html) == '<html></html>'

    # Test 2: Head element
    head = Head()
    assert str(head) == '<head></head>'

    # Test 3: Body element
    body = Body()
    assert str(body) == '<body></body>'

    # Test 4: Title element with content
    title = Title(Text("Test Title"))
    assert str(title) == '<title>\n  Test Title\n</title>'

    # Test 5: Meta element with attributes
    meta = Meta({'charset': 'UTF-8'})
    assert str(meta) == '<meta charset="UTF-8">'

    # Test 6: Img element with attributes
    img = Img({'src': 'image.png', 'alt': 'Test Image'})
    assert str(img) == '<img src="image.png" alt="Test Image">' or str(img) == '<img alt="Test Image" src="image.png">'

    # Test 7: Table element
    table = Table()
    assert str(table) == '<table></table>'

    # Test 8: Th element with content
    th = Th(Text("Header"))
    assert str(th) == '<th>\n  Header\n</th>'

    # Test 9: Tr element
    tr = Tr()
    assert str(tr) == '<tr></tr>'

    # Test 10: Td element with content
    td = Td(Text("Data"))
    assert str(td) == '<td>\n  Data\n</td>'

    # Test 11: Ul element
    ul = Ul()
    assert str(ul) == '<ul></ul>'

    # Test 12: Ol element
    ol = Ol()
    assert str(ol) == '<ol></ol>'

    # Test 13: Li element with content
    li = Li(Text("List item"))
    assert str(li) == '<li>\n  List item\n</li>'

    # Test 14: H1 element with content
    h1 = H1(Text("Header 1"))
    assert str(h1) == '<h1>\n  Header 1\n</h1>'

    # Test 15: H2 element with content
    h2 = H2(Text("Header 2"))
    assert str(h2) == '<h2>\n  Header 2\n</h2>'

    # Test 16: P element with content
    p = P(Text("Paragraph"))
    assert str(p) == '<p>\n  Paragraph\n</p>'

    # Test 17: Div element
    div = Div()
    assert str(div) == '<div></div>'

    # Test 18: Span element with content
    span = Span(Text("Span text"))
    assert str(span) == '<span>\n  Span text\n</span>'

    # Test 19: Hr element
    hr = Hr()
    assert str(hr) == '<hr>'

    # Test 20: Br element
    br = Br()
    assert str(br) == '<br>'

    print("All basic tests passed!")

def complex_test():
    # Test 21: Html with Head and Body
    html = Html([Head(), Body()])
    assert str(html) == '<html>\n  <head></head>\n  <body></body>\n</html>'

    # Test 22: Body with nested elements
    body = Body([H1(Text("Header 1")), P(Text("Paragraph"))])
    assert str(body) == '<body>\n  <h1>\n    Header 1\n  </h1>\n  <p>\n    Paragraph\n  </p>\n</body>'

    # Test 23: Table with rows and cells
    table = Table([Tr([Td(Text("Cell 1")), Td(Text("Cell 2"))]), Tr([Td(Text("Cell 3")), Td(Text("Cell 4"))])])
    assert str(table) == '<table>\n  <tr>\n    <td>\n      Cell 1\n    </td>\n    <td>\n      Cell 2\n    </td>\n  </tr>\n  <tr>\n    <td>\n      Cell 3\n    </td>\n    <td>\n      Cell 4\n    </td>\n  </tr>\n</table>'

    # Test 24: Nested Divs
    div = Div([Div([P(Text("Nested Paragraph"))])])
    assert str(div) == '<div>\n  <div>\n    <p>\n      Nested Paragraph\n    </p>\n  </div>\n</div>'

    # Test 25: Ul with Li elements
    ul = Ul([Li(Text("Item 1")), Li(Text("Item 2")), Li(Text("Item 3"))])
    assert str(ul) == '<ul>\n  <li>\n    Item 1\n  </li>\n  <li>\n    Item 2\n  </li>\n  <li>\n    Item 3\n  </li>\n</ul>'

    # Test 26: Ol with Li elements
    ol = Ol([Li(Text("First")), Li(Text("Second")), Li(Text("Third"))])
    assert str(ol) == '<ol>\n  <li>\n    First\n  </li>\n  <li>\n    Second\n  </li>\n  <li>\n    Third\n  </li>\n</ol>'

    # Test 27: Div with multiple elements
    div = Div([H1(Text("Header")), P(Text("Paragraph")), Img({'src': 'image.png', 'alt': 'Image'})])
    assert str(div) == '<div>\n  <h1>\n    Header\n  </h1>\n  <p>\n    Paragraph\n  </p>\n  <img src="image.png" alt="Image">\n</div>' or str(div) == '<div>\n  <h1>\n    Header\n  </h1>\n  <p>\n    Paragraph\n  </p>\n  <img alt="Image" src="image.png">\n</div>'

    print("All complex tests passed!")

def main():
    basic_test()
    complex_test()
    html = Html([
        Head(Title(Text('"Hello ground!"'))),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img({'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    print(html)
    # with open('elements.html', 'w') as f:
    #     f.write(str(html))

if __name__ == '__main__':
    main()