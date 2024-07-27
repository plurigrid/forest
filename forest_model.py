import os

class DirectoryNode:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"DirectoryNode(name={self.name}, path={self.path}, children={len(self.children)})"

def build_directory_tree(root_path):
    root_node = DirectoryNode(name=os.path.basename(root_path), path=root_path)
    for dirpath, dirnames, filenames in os.walk(root_path):
        current_node = DirectoryNode(name=os.path.basename(dirpath), path=dirpath)
        for dirname in dirnames:
            child_node = DirectoryNode(name=dirname, path=os.path.join(dirpath, dirname))
            current_node.add_child(child_node)
        for filename in filenames:
            child_node = DirectoryNode(name=filename, path=os.path.join(dirpath, filename))
            current_node.add_child(child_node)
        if dirpath == root_path:
            root_node = current_node
    return root_node

def print_directory_tree(node, indent=""):
    print(indent + node.name)
    for child in node.children:
        print_directory_tree(child, indent + "  ")

if __name__ == "__main__":
    root_path = "."  # Change this to the desired root path
    directory_tree = build_directory_tree(root_path)
    print_directory_tree(directory_tree)
