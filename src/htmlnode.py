from functools import reduce

class HTMLNode:
    def __init__(self,
                 tag = None, value = None,
                 children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedErrpr()

    def props_to_html(self):
        if self.props is None:
            return ""

        html = reduce(lambda s, x: f'{s} "{x[0]}"="{x[1]}"',
                      self.props.items(),
                      "")
        return html
    
    def __repr__(self):
        s = f'tag: {self.tag}\n'
        s += f'value: {self.value}\n'
        s += f'props: {repr(self.props)}\n'
        s += f'children: {repr(self.children)}\n'
        return s

