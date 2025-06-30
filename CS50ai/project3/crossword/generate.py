import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable in self.domains:
            words = self.domains[variable].copy()
            for word in words:
                if variable.length != len(word):
                    self.domains[variable].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        # Get the words in respective domains
        words_x = self.domains[x].copy()
        words_y = self.domains[y].copy()

        # Track if any revision made
        revised = 0

        # Check overlap
        if self.crossword.overlaps[x, y]:
            i, j = self.crossword.overlaps[x, y]

            # Remove arc inconsistent words from domain of `x`
            for w1 in words_x:
                found = 0
                for w2 in words_y:
                    if w1[i] == w2[j]:
                        found = 1
                        break
                if not found:
                    self.domains[x].remove(w1)
                    revised = 1

        if revised:
            return True
        else:
            return False

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        # Create all possible arcs if arcs is empty
        if arcs is None:
            arcs = []
            for x in self.domains:
                for y in self.domains:
                    # Check overlap
                    if (x != y) and (self.crossword.overlaps[x, y]):
                        arc = (x, y)
                        # Add arc
                        arcs.append(arc)

        # Loops through arcs until queue is empty
        while arcs:

            # Make variable arc consistent
            arc = arcs.pop(0)
            x, y = arc
            revised = self.revise(x, y)
            if revised:
                # Empty domain, No solution possible
                if len(self.domains[x]) == 0:
                    return False
                # Add new arcs to list if variable is revised
                neighbors = self.crossword.neighbors(x)
                for neighbor in neighbors:
                    arc = (neighbor, x)
                    arcs.append(arc)

        # All variables are arc consistent
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        # Loop through all variables
        for variable in self.domains:

            # Assigment incomplete
            if variable not in assignment or not assignment[variable]:
                return False

        # Assignment complete
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        # Loop through each variable present in assignment
        for variable in assignment:

            # Check if all values are distinct
            if len(assignment) != len(set(assignment.values())):
                return False

            # Check if all values are of correct length
            if len(assignment[variable]) != variable.length:
                return False

            # Check for conflict with neighbours
            neighbors = self.crossword.neighbors(variable)
            for neighbor in neighbors:
                if neighbor in assignment:
                    i, j = self.crossword.overlaps[variable, neighbor]
                    if assignment[variable][i] != assignment[neighbor][j]:
                        return False

        # Assignment is consistent
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        # Get neighbors
        neighbors = self.crossword.neighbors(var)

        # Get words from domain
        words = self.domains[var]

        # Empty dictionary to store 'words : elimiminations'
        eliminations = {}

        # For every word in domain, calculates the number of elimination(n)
        for word in words:
            n = 0
            for neighbor in neighbors:
                if neighbor not in assignment:
                    i, j = self.crossword.overlaps[var, neighbor]
                    neighbor_words = self.domains[neighbor]
                    for w in neighbor_words:
                        if word[i] != w[j]:
                            n += 1

            # Add 'word' and corresponding 'eliminations' to dictionary
            eliminations[n] = word

        # Sort values in ascending order
        eliminations = dict(sorted(eliminations.items()))
        values = list(eliminations.values())

        return values

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        # Get unassigned variables
        unassign_var = []
        for variable in self.domains:
            if variable not in assignment:
                unassign_var.append(variable)

        # Map the number of remaining values to each unassigned variable
        # as '(number, variable)' tuple
        rem_val = []
        for variable in unassign_var:
            num = len(self.domains[variable])
            rem_val.append((num, variable))
        # Sort by number of remaining values
        rem_val = sorted(rem_val, key=lambda x: x[0])

        # No Tie (among number of remaining values)
        if len(rem_val) == 1:
            return rem_val[0][1]
        else:
            num1 = rem_val[0][0]
            num2 = rem_val[1][0]
            if num1 != num2:
                return rem_val[0][1]

        # List of variable with same number of remaining values
        var = []
        min_val = rem_val[0][0]
        for item in rem_val:
            if item[0] == min_val:
                var.append(item[1])
            else:
                break

        # Get degree of each variable
        degree = []
        for variable in var:
            deg = self.crossword.neighbors(variable)
            degree.append((deg, variable))

        # Return varibale with least degree
        degree = sorted(degree, key=lambda x: x[0])
        return degree[0][1]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        if self.assignment_complete(assignment):
            return assignment
        else:
            var = self.select_unassigned_variable(assignment)
            for word in self.domains[var]:
                assignment[var] = word
                if self.consistent(assignment):
                    result = self.backtrack(assignment)
                    if result is not None:
                        return result
                del assignment[var]

            return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
