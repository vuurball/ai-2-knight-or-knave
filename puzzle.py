from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

rules = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
)

print('Puzzle 0:')
print('    > A says "I am both a knight and a knave."')
sent1 = And(AKnight,AKnave)
knowledge0 = And(
    rules,
    Biconditional(AKnight, sent1)
)

print('Puzzle 1:')
print('    > A says "We are both knaves."')
print('    > B says nothing.')
sent1 = And(AKnave, BKnave)

knowledge1 = And(
    rules, 
    Biconditional(AKnight, sent1)
)

print('Puzzle 2:')
print('    > A says "We are the same kind."')
print('    > B says "We are of different kinds."')
sent1 = Or(And(AKnave, BKnave), And(AKnight, BKnight))
sent2 = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    rules,
    Biconditional(AKnight, sent1),
    Biconditional(BKnight, sent2)
)

print('Puzzle 3:')
print('    > A says either "I am a knight." or "I am a knave.", but you dont know which.')
print('    > B says "A said `I am a knave`.')
print('    > B says "C is a knave.')
print('    > C says "A is a knight.')

sent2 = And(AKnight, AKnave)
sent3 = CKnave
sent4 = AKnight

knowledge3 = And(
    rules,
    Biconditional(BKnight, sent2),
    Biconditional(BKnight, sent3),
    Biconditional(CKnight, sent4),
)

print('Puzzle 4:')
print('    > A says "B and I are the same.')
print('    > B says "C is a knave')
print('    > C says "A and C are different.')

sent1 = Or(And(BKnight, AKnight), And(BKnave, AKnave))
sent2 = CKnave
sent3 = Or(And(AKnight, CKnave), And(AKnave, CKnight))

knowledge4 = And(
    rules,
    Biconditional(AKnight, sent1),
    Biconditional(BKnight, sent2),
    Biconditional(CKnight, sent3),
)

print("")

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
        ("Puzzle 4", knowledge4)
    ]
    print("SOLUTIONS:")
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
