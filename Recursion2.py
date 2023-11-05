def squares(square):
    if square < 1:
        return 1
    else: return 2 * (square - 1) + squares(square - 1)

print(squares(0))