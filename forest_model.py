import os
import random

class DirectoryNode:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.children = []
        self.content = None

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
            with open(os.path.join(dirpath, filename), 'r') as f:
                child_node.content = f.read()
            current_node.add_child(child_node)
        if dirpath == root_path:
            root_node = current_node
    return root_node

def print_directory_tree(node, indent=""):
    print(indent + node.name)
    for child in node.children:
        print_directory_tree(child, indent + "  ")

def random_walk(node, steps=5):
    current_node = node
    path = [current_node]
    for _ in range(steps):
        if current_node.children:
            current_node = random.choice(current_node.children)
            path.append(current_node)
        else:
            break
    return path

def extract_wisdom(node):
    if node.content:
        # This is a simple example. In a real implementation, you'd use more sophisticated NLP techniques.
        sentences = node.content.split('.')
        if sentences:
            return random.choice(sentences).strip()
    return "No wisdom found in this file."

if __name__ == "__main__":
    root_path = "."  # Change this to the desired root path
    directory_tree = build_directory_tree(root_path)
    print_directory_tree(directory_tree)
    
    random_path = random_walk(directory_tree)
    print("\nRandom walk:")
    for node in random_path:
        print(node.name)
        if node.content:
            print("Wisdom:", extract_wisdom(node))
