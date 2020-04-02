def main():
    import random
    print(random.randint(5, 20))  # line 1
    """What did you see on line 1?
        An integer from 5 to 20(20 is not included)
        What was the smallest number you could have seen, what was the largest?
        The smallest is 5,The largest is 19"""
    print(random.randrange(3, 10, 2))  # line 2
    """What did you see on line 2?
       An odd number from 3 to 10
       What was the smallest number you could have seen, what was the largest?
       The smallest is 3,The largest number is 9
       Could line 2 have produced a 4?
       No"""
    print(random.uniform(2.5, 5.5))  # line 3
    """What did you see on line 3?
       A real number from 2.5 to 5.5(5.5 not included) 
       What was the smallest number you could have seen, what was the largest?
       The smallest number is 2.5, The largest number is going to infinitely close to 5.5"""

    print(random.randint(1, 101))

if __name__ == '__main__':
    main()