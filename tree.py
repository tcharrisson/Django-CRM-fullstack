from pathlib import Path

def print_tree(root, indent=""):
    for path in sorted(Path(root).rglob("*")):
        depth = len(path.relative_to(root).parts)
        spacer = "    " * depth
        print(f"{spacer}{path.name}")

print_tree("dcrm")
python tree.py > project_structure.txt
