class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ''

        return ' '.join(
            f'{key}="{value}"'
            for key, value in self.props.items()
        )

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag,value, None, props)

    def to_html(self):
        if self.value is None and self.tag != "img":
            raise ValueError
        elif self.tag is None:
            return self.value
        else:
            if self.tag == "img":
                return f'<{self.tag} {self.props_to_html()}/>'
            else:
                if self.props is None:
                    return f'<{self.tag}>{self.value}</{self.tag}>'
                else:
                    return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode(tag={self.tag}, children={self.children})'

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        to_html_string = ""
        
        if self.tag is None:
            raise ValueError
        elif self.children is None:
            raise ValueError("No children nodes provided")
        else:
            for i in self.children:
                to_html_string += i.to_html()

        return f'<{self.tag}{self.props_to_html()}>{to_html_string}</{self.tag}>'