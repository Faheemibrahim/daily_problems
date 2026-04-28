# Problem: Write print_tree(node, depth=0) to visualise the KD-tree structure.
# Concept: A recursive tree printer is one of the most useful debugging tools you can
#          have when implementing tree-based algorithms. The indentation level shows depth.
# You are done when:
#   [ ] The root appears at indent level 0
#   [ ] Each level of depth adds 2 or 4 spaces of indentation
#   [ ] Left and right children are clearly labelled
#   [ ] The output matches the expected format in tests
# Hint: print("  " * depth + f"[axis={node.axis}] {node.point}") then recurse on children.


class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point, self.axis, self.left, self.right = point, axis, left, right


def build_kdtree(points, depth=0):
    if not points: return None
    axis = depth % 3
    points = sorted(points, key=lambda p: p[axis])
    mid = len(points) // 2
    return KDNode(points[mid], axis,
                  build_kdtree(points[:mid], depth+1),
                  build_kdtree(points[mid+1:], depth+1))


def print_tree(node, depth=0, label="root"):
    """
    Print the tree structure with indentation showing depth.
    Format each line as: {indent}[{label}] axis={axis} point={point}
    where indent = "  " * depth.
    Return a list of strings (one per node) for testing.
    """
    pass


if __name__ == "__main__":
    pts = [(5.0, 0.0, 0.0), (2.0, 0.0, 0.0), (8.0, 0.0, 0.0)]
    root = build_kdtree(pts)
    lines = print_tree(root)

    print("PASS num lines" if len(lines) == 3 else f"FAIL num lines — {len(lines)}: {lines}")
    print("PASS root label" if "root" in lines[0] else f"FAIL root label — {lines[0]}")
    has_indent = any(line.startswith("  ") for line in lines[1:])
    print("PASS indented children" if has_indent else f"FAIL indent — {lines}")
