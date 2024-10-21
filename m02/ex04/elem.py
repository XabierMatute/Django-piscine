#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    [...]
    class ValidationError(Exception):
        """
        A custom exception to raise when a ValidationError occurs.
        """
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if not isinstance(tag, str) or not isinstance(attr, dict):
            raise Elem.ValidationError
        if tag_type not in ['double', 'simple']:
            raise Elem.ValidationError
        
        self.tag = tag
        self.attr = attr
        self.content = [] if content is None else content
        if not isinstance(self.content, list):
            self.content = [self.content]
        if content is not None and not Elem.check_type(content):
            raise Elem.ValidationError
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = self.open_tag() + self.__make_content() + self.close_tag()
        elif self.tag_type == 'simple':
            result = self.open_tag()
        return result

    def open_tag(self):
        return '<' + self.tag + self.__make_attr() + '>'
    
    def close_tag(self):
        return '</' + self.tag + '>'

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        # Filtrar los elementos vacíos de self.content
        self.content = [content for content in self.content if str(content) != '']
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += '  ' + str(elem).replace('\n', '\n  ') + '\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


def main():
    """
    Just a main function to test this class.
    """
    html = Elem(tag='html', content=[
        Elem(tag='head', content=[
            Elem(tag='title', content=Text('"Hello ground!"'))
        ]),
        Elem(tag='body', content=[
            Elem(tag='h1', content=Text('"Oh no, not again!"')),
            Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ])
    ])
    print(html)
    # with open('elem.html', 'w') as f:
    #     f.write(str(html))

if __name__ == '__main__':
    main()
