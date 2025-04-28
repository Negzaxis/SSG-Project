




class HTMLNode:
    def __init__ (self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception("NotImplementedError")
    
    def props_to_html(self):
        props_list = []
        if self.props == None:
            return ""
        for key, value in self.props.items():
            props_list.append(f' {key}="{value}"')
        seperator = ""
        return seperator.join(props_list)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    

