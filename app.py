from flask import Flask, jsonify
from forest_model import build_directory_tree, random_walk, extract_wisdom

app = Flask(__name__)

@app.route('/random-walk')
def perform_random_walk():
    root_path = "."  # Change this to the desired root path
    directory_tree = build_directory_tree(root_path)
    walk_result = random_walk(directory_tree)
    
    result = {
        "path": [
            {
                "name": node.name,
                "wisdom": extract_wisdom(node) if node.content else None
            } for node in walk_result
        ]
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
