from textnode import TextType, TextNode

def main():
    print("hello world")
    text_node = TextNode("This is text", TextType.TEXT)
    print(repr(text_node))

if __name__ == "__main__":
    main()
