import sys
number_of_moves = 0

def move(n, source, destination, auxiliary):
    global number_of_moves
    if n > 0:
        move(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        number_of_moves += 1
        move(n - 1, auxiliary, destination, source)


try:
    if len(sys.argv) != 2:
        raise ValueError("Exactly one argument is required")
    if not sys.argv[1].isdigit():
        raise ValueError("The argument must be a positive integer")
    number_of_disks = int(sys.argv[1])
    if number_of_disks <= 1 or number_of_disks > 20:
        raise ValueError(
            "The argument must be between 1 and 20, inclusive")
    move(number_of_disks, "A", "B", "C")
    print(f"\nTotal number of moves made: {number_of_moves}")
except ValueError as e:
    print(f"Error: {e}")
