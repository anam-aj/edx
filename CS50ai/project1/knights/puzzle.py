from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
A_says = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnave, Not(A_says)),
    Implication(AKnight, A_says)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_says = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    Implication(AKnave, Not(A_says)),
    Implication(AKnight, A_says)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_says = Or(And(AKnave, BKnave), And(AKnight, BKnight))
B_says = Not(A_says)
knowledge2 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Implication(AKnave, Not(A_says)),
    Implication(AKnight, A_says),
    Implication(BKnave, Not(B_says)),
    Implication(BKnight, B_says)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A_says = Or(AKnight, AKnave)
B_says1 = Implication(A_says, AKnave)
B_says2 = CKnight
B_says = And(B_says1, B_says2)
C_says = AKnight
knowledge3 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnave, CKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    Not(And(CKnave, CKnight)),
    Implication(AKnave, Not(A_says)),
    Implication(AKnight, A_says),
    Implication(BKnave, Not(B_says)),
    Implication(BKnight, B_says),
    Implication(CKnave, Not(C_says)),
    Implication(CKnight, C_says)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
