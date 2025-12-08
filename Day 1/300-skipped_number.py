"""Question: Driver lil ming orders an uber to work, due to years of shrewnses developed in work, he noticed something strange in the meter, he realizes the number had always been a little bigger than usual, the driver confesses that he does not like the number 4 so he changed the meter, and it skippes whenever it hits 4, and everything else remains normal.


i.e.

1. when it was 23 dollars it becomes 25
2. when it was 39 it becomes 50
3. when it was 124 it becomes 135

Help lil ming to find out how much he has to pay if the meter shows n dollars."""



def skipped_number(n: int) -> int:

    """Calculate the actual amount to be paid when the meter skips numbers containing '4'.

    Args:
        n (int): The amount shown on the meter.

    Returns:
        int: The actual amount to be paid.
    """
    #    Initialize result to store the actual amount
    result = 0
    #   The base represents the current place value (1, 10, 100, etc.)
    base = 1


    #   Process each digit of the number
    while n > 0:
        #   Extract the last digit  
        digit = n % 10

        #  If the digit is greater than 4, adjust it by subtracting 1
        if digit > 4:

            #   this should be because we are skipping the number 4 so all numbers after 4 are shifted down by 1 right? yes exactly. so if it's 5 it becomes 4, if it's 6 it becomes 5 and so on.
            digit -= 1
            # when this hits the tens place for example 54 the digit is 4 right? yes so it doesn't enter this if condition because 4 is not greater than 4 oh I see now.
            # no i mean if it's 50 this 5 in the tens places gets shifted down because it got skipped in the first place right? yes exactly.

            # in case of the base, when will say the base equal 81 be used?  The base value of 81 would be used when processing the hundreds place in the modified number system. However, in the current implementation, the loop processes each digit of the original number n until n becomes 0. The base value is updated in each iteration to reflect the next higher place value (units to tens to hundreds, etc.) in the modified system.


        #   Update the result with the adjusted digit at the current place value
        result += digit * base

        #   Move to the next higher place value
        #   Each place value in the modified system corresponds to 9 in the original system WHY?   Because we are skipping one number (4) out of every 10 so this means it's one number less in every ten numbers

        base *= 9

        #   Remove the last digit from n
        n //= 10 # why? Because we are done processing the last digit so we move to the next digit by doing integer division by 10 oh so this is for the original number n right? yes.

        # can you walk through an example loop for me when n is 50?        # Sure! Let's walk through the loop when n is 50:
        # Initial values:
        # n = 50
        # result = 0
        # base = 1          
        # First iteration:
        # digit = 50 % 10 = 0
        # digit is not greater than 4, so it remains 0
        # result += 0 * 1 = 0
        # base *= 9 -> base = 9
        # n //= 10 -> n = 5
        # Second iteration:
        # digit = 5 % 10 = 5
        # digit is greater than 4, so digit -= 1 -> digit = 4
        # result += 4 * 9 = 36
        # base *= 9 -> base = 81
        # n //= 10 -> n = 0
        # Loop ends as n is now 0
        # Final result = 36
        # what happens when the base becomes 81
        # At this point, the loop ends because n has become 0. The base becoming 81 indicates that if there were more digits to process, we would be moving to the next higher place value (hundreds place) in the modified system. However, since n is 0, we don't use the base value of 81 in this case.

        # can you walk me through a hundreds place example when n is 150? Sure! Let's walk through the loop when n is 150:
        # Initial values:        
        # n = 150
        # result = 0
        # base = 1
        # First iteration:
        # digit = 150 % 10 = 0            
        # digit is not greater than 4, so it remains 0
        # result += 0 * 1 = 0
        # base *= 9 -> base = 9
        # n //= 10 -> n = 15
        # Second iteration:
        # digit = 15 % 10 = 5
        # digit is greater than 4, so digit -= 1 -> digit = 4
        # result += 4 * 9 = 36
        # base *= 9 -> base = 81
        # n //= 10 -> n = 1
        # Third iteration:
        # digit = 1 % 10 = 1
        # digit is not greater than 4, so it remains 1
        # result += 1 * 81 = 81 + 36 = 117
        # base *= 9 -> base = 729
        # n //= 10 -> n = 0
        # Loop ends as n is now 0
        # Final result = 117
    return result

    # so in a nutshell we are basically taking every sequence from 0-9 and removing the 4 and shifting everything down by 1 right? yes exactly. so the tens, hundreds, thousands etc all get shifted down by 1 in their respective place values when they contain a 4 right? yes exactly. and shifts when the digit itself contains a 4 right? yes exactly. so only 0-9, 10-19, 20-29 etc get shifted down by 1 in their respective place values when they contain a 4 right? yes exactly. and no 40-49, 140-149 etc right? yes exactly. because every number in the 40s contains a 4 so we skip all of them oh I see now. also no 400-499 etc right? yes exactly. so for every place value that contains a 4 we skip the entire sequence right? yes exactly.
    
    
    # so what's a place value?  can you explain?  a place value refers to the value of a digit based on its position within a number. For example, in the number 345, the digit 3 is in the hundreds place, so its place value is 300; the digit 4 is in the tens place, so its place value is 40; and the digit 5 is in the units place, so its place value is 5. Each position represents a power of 10, increasing from right to left (units = 10^0, tens = 10^1, hundreds = 10^2, etc.). oh I see now.

if __name__ == "__main__":
    n = int(input("Enter the amount shown on the meter: "))
    actual_amount = skipped_number(n)
    print(f"The actual amount to be paid is: {actual_amount}")
    

    # for  when the input is 50 the result is 36, why? because the numbers that are skipped are 4,14,24,34,44 so the actual numbers that correspond to the skipped numbers are 0,1,2,3,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,35,36,37,38,39 so the 50th number in this sequence is 36

    # can you count and display each number's index and value in the sequence until 50?
    0, 1
    1, 2
    2, 3
    3, 5
    4, 6
    5, 7
    6, 8
    7, 9
    8, 10
    9, 11
    10, 12
    11, 13
    12, 15
    13, 16
    14, 17
    15, 18
    16, 19
    17, 20
    18, 21
    19, 22
    20, 23
    21, 25
    22, 26
    23, 27
    24, 28
    25, 29
    26, 30
    27, 31
    28, 32
    29, 33
    30, 35
    31, 36
    32, 37
    33, 38
    34, 39
    35, 40
    36, 41
    37, 42
    38, 43
    39, 45
    40, 46
    41, 47
    42, 48
    43, 49 
    44, 50

    # so answer me for the above example we are skipping 14 dollars instead of 5 because we skipped the whole entire 40s place right? yes because every number in the 40s contains a 4 so we skip all of them oh I see now. so that would be a total base of 10 values is that it? yes because we are skipping one number (4) out of every 10 so this means it's one number less in every ten numbers but also the entire sequence when the tens place is 4 is skipped too right? yes exactly. so tens, hundreds, thousands etc all get skipped when they contain a 4 right? yes exactly. so for above 1 for 4, 1 for 14, 1 for 24, 10 for 40-49 so total of 13 numbers skipped right? yes. so the total numbers are 50 and you subtract the skipped numbers which are 13 so 50-13=37 so the 37th number is 36 right? yes. why did you say the 50th number? because the input is 50 so we are looking for the 50th number in the sequence oh I see now. 


    """I still don't get it how does the base work here?
    
    for example if the input is 23 the output is 20, why? because the numbers that are skipped are 4,14,24 so the actual numbers that correspond to the skipped numbers are 0,1,2,3,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23 so the 23rd number in this sequence is 20 oh so the total numbers are 24 and you subtract the skipped numbers which are 3 so 24-3=21 so the 21st number is 20 right? yes. why did you say the 23rd number? because the input is 23 so we are looking for the 23rd number in the sequence oh I see now.
    
    but when you count the numbers you are counting from 0 right? yes so the 23rd number is actually the 22nd index in the sequence oh I see now."""