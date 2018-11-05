class Tag:

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!A LONG DOCTYPE STRING', '')
        self.end_tag = ''


class Title(Tag):

    def __init__(self, title):
        super().__init__('title', title)


class Head(Tag):

    def __init__(self, title):
        super().__init__('head', '')
        if title:
            self.contents = Title(title)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc:

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    # my_page = HtmlDoc('horej')
    # my_page.add_tag('h1', 'Main heading')
    # my_page.add_tag('h2', 'Secondary heading')
    # my_page.add_tag('p', 'A paragraph')
    # with open('test.html', 'w') as test_doc:
    #     my_page.display(file=test_doc)

    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                          "of objects to build up another object")
    new_body.add_tag('p', "The composed object doesnt need to actually own the objects that it's composed of"
                          " - if it's destroyed, those objects continue to exist")

    new_doctype = DocType()
    new_header = Head('Aggregation doc')
    my_page = HtmlDoc(new_doctype, new_header, new_body)


# give our document new content by switching it's body
    with open('test2.html', 'w') as test_doc:
        my_page.display(file=test_doc)

