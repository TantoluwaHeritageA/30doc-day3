def checkpalindrome(end):
    count_pal_num = 0
    count_non_pal_num = 0
    for i in range(1, end):
        num = str(i)
        rev_num = num[::-1]
        if num == rev_num:
            count_pal_num = count_pal_num + 1
            print(rev_num, "is a palindrome")
        elif num != rev_num:
            count_non_pal_num += 1

    print("The total numbers of formed palindrome is: ", count_pal_num)
    print("The total numbers of non-palindromic digits are: ", count_non_pal_num)


checkpalindrome(500)
