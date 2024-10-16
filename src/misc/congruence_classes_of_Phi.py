from sympy.ntheory.factor_ import totient

if __name__ == "__main__":
    zero_mod_eleven = 0
    one_mod_eleven = 0
    two_mod_eleven = 0
    three_mod_eleven = 0
    four_mod_eleven = 0
    five_mod_eleven = 0
    five_mod_eleven = 0
    six_mod_eleven = 0
    seven_mod_eleven = 0
    eight_mod_eleven = 0
    nine_mod_eleven = 0
    ten_mod_eleven = 0

    for n in range(1, 100):
        out = 0

        for i in range(1, n + 1):
            out += totient(i)

        if out % 11 == 0:
            zero_mod_eleven += 1
        elif out % 11 == 1:
            one_mod_eleven += 1
        elif out % 11 == 2:
            two_mod_eleven += 1
        elif out % 11 == 3:
            three_mod_eleven += 1
        elif out % 11 == 4:
            four_mod_eleven += 1
        elif out % 11 == 5:
            five_mod_eleven += 1
        elif out % 11 == 6:
            six_mod_eleven += 1
        elif out % 11 == 7:
            seven_mod_eleven += 1
        elif out % 11 == 8:
            eight_mod_eleven += 1
        elif out % 11 == 9:
            nine_mod_eleven += 1
        elif out % 11 == 10:
            ten_mod_eleven += 1

        print(out, (n * (n + 1)) / 3)

        # print(f"out mod 11 = {out % 11}")

    # print(
    #     zero_mod_eleven,
    #     one_mod_eleven,
    #     two_mod_eleven,
    #     three_mod_eleven,
    #     four_mod_eleven,
    #     five_mod_eleven,
    #     six_mod_eleven,
    #     seven_mod_eleven,
    #     eight_mod_eleven,
    #     nine_mod_eleven,
    #     ten_mod_eleven,
    # )
