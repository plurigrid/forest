import unittest
from forest_model import DirectoryNode, build_directory_tree, print_directory_tree, random_walk, extract_wisdom

class TestForest(unittest.TestCase):
    def setUp(self):
        self.root = DirectoryNode("root", "/root")
        self.child1 = DirectoryNode("child1", "/root/child1")
        self.child2 = DirectoryNode("child2", "/root/child2")
        self.root.add_child(self.child1)
        self.root.add_child(self.child2)
        self.child1.content = "This is child1 content."
        self.child2.content = "This is child2 content."

    def test_build_directory_tree(self):
        # This test would require a mock file system
        pass

    def test_print_directory_tree(self):
        # Redirect stdout to capture print output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_directory_tree(self.root)
        sys.stdout = sys.__stdout__
        expected_output = "root\n  child1\n  child2\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_random_walk(self):
        path = random_walk(self.root)
        self.assertGreater(len(path), 0)
        self.assertEqual(path[0], self.root)

    def test_extract_wisdom(self):
        wisdom = extract_wisdom(self.child1)
        self.assertEqual(wisdom, "This is child1 content.")

if __name__ == '__main__':
    unittest.main()
