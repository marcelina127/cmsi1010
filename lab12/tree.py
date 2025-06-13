from math import pi, radians as rad
from Tree.core import Tree
from PIL import Image

branches = (
    (.1, rad(-30)),
    (.2, rad(30)),
    (.7, rad(60))
)

def main():
    tree = Tree(
        pos=(0, 0, 0, -500),
        branches=branches
    )

    # Let the tree grow
    tree.grow(10)

    # Move the tree in the right position, so that the tree is completly in the image
    tree.move_in_rectangle()

    im = Image.new("RGB", tree.get_size(), (239, 239, 239))
    tree.draw_on(im, (85, 25, 0, 128, 53, 21), (0, 62, 21), 10)
    im.show()

if __name__ == '__main__':
    main()