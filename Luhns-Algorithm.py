def verify_card_number(card_number):
    # Initialize the sum of digits
    total_sum = 0
    card_number_reversed = card_number[::-1]  # Reverse the card number for easier processing
    
    # Iterate over all digits, processing odd and even indexed digits
    for i, digit in enumerate(card_number_reversed):
        num = int(digit)
        
        # If the index is odd (0-based index, so it's even position in the original number)
        if i % 2 == 1:
            num *= 2  # Double the digit
            if num >= 10:
                num = num - 9  # Subtract 9 if the result is greater than or equal to 10
        
        total_sum += num
    
    # If the total sum modulo 10 is 0, the card number is valid
    return total_sum % 10 == 0

def main():
    # Example card number
    card_number = '5500-0000-0000-0004'
    
    # Remove dashes and spaces from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Verify the card number and print the result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

if __name__ == '__main__':
    main()
