def condense_roman_numeral(roman_numeral):
    roman_numeral = roman_numeral.replace('LXXXX', 'XC')
    roman_numeral = roman_numeral.replace('XXXX', 'XL')
    roman_numeral = roman_numeral.replace('VIIII', 'IX')
    roman_numeral = roman_numeral.replace('IIII', 'IV')
    roman_numeral = roman_numeral.replace('DCCCC', 'CM')
    roman_numeral = roman_numeral.replace('CCCC', 'CD')
    return roman_numeral

def main():
    test_result(condense_roman_numeral("IIII"), "IV")
    test_result(condense_roman_numeral("VIIII"), "IX")

    test_result(condense_roman_numeral("XXXX"), "XL")
    test_result(condense_roman_numeral("LXXXX"), "XC")

    test_result(condense_roman_numeral("DCCCC"), "CM")
    test_result(condense_roman_numeral("CCCC"), "CD")

def test_result(a, b):
    if (a == b):
        print("Success!")
    else:
        print("Fail")
        print("Value a was: " + a)
        print("Value b was: " + b)

if __name__ == "__main__":
    main()