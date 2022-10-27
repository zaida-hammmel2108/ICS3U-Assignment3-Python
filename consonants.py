#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: October 2022
# This program detects if your letter is a consonant or vowel


def main():
    # this function checks if your letter is a consonant or vowel
    # input
    user_letter = input("Enter any letter in lowercase(a-z): ")
    print("")

    # process & output
    match user_letter:
        case "a":
            print("Your letter is a vowel.")
        case "b":
            print("Your letter is a consonant.")
        case "c":
            print("Your letter is a consonant.")
        case "d":
            print("Your letter is a consonant.")
        case "e":
            print("Your letter is a vowel.")
        case "f":
            print("Your letter is a consonant.")
        case "g":
            print("Your letter is a consonant.")
        case "h":
            print("Your letter is a consonant.")
        case "i":
            print("Your letter is a vowel.")
        case "j":
            print("Your letter is a consonant.")
        case "k":
            print("Your letter is a consonant.")
        case "l":
            print("Your letter is a consonant.")
        case "m":
            print("Your letter is a consonant.")
        case "n":
            print("Your letter is a consonant.")
        case "o":
            print("Your letter is a vowel.")
        case "p":
            print("Your letter is a consonant.")
        case "q":
            print("Your letter is a consonant.")
        case "r":
            print("Your letter is a consonant.")
        case "s":
            print("Your letter is a consonant.")
        case "t":
            print("Your letter is a consonant.")
        case "u":
            print("Your letter is a vowel.")
        case "v":
            print("Your letter is a consonant.")
        case "w":
            print("Your letter is a consonant.")
        case "x":
            print("Your letter is a consonant.")
        case "y":
            print("Your letter is a sometimes a consonant and sometimes a vowel.")
        case "z":
            print("Your letter is a consonant.")
        case "_":
            print("Invalid letter.")

    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
