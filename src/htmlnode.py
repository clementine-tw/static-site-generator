from functools import reduce


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedErrpr()

    def props_to_html(self):
        if self.props is None:
            return ""

        html = reduce(lambda s, x: f'{s} "{x[0]}"="{x[1]}"', self.props.items(), "")
        return html

    def __repr__(self):
        s = f"tag: {self.tag}\n"
        s += f"value: {self.value}\n"
        s += f"props: {repr(self.props)}\n"
        s += f"children: {repr(self.children)}\n"
        return s


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes muse have a value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        children_html = reduce(
            lambda pre, child: pre + child.to_html(), self.children, ""
        )
        html = f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        return html
