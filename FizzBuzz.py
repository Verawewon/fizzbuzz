def main():
    # 1
    # 2

    for i in range(1,101):
        if i % 15==0:
            print("FizzBuzz")
        elif i % 3==0:
            print("Fizz")
        elif i % 5==0:
            print("Buzz")
        else:
            print(i)


    for i in range(1,101):
        if i==42:
            print("Answer to the Ultimate Question of Life, the Universe, and Everything")
        else:
            if i % 3==0:
                print("Fizz", end="")
            if i % 5==0:
                print("Buzz", end="")
            if i % 3 !=0 and i % 5 !=0:
                print(i,end="")
            print()



if __name__ == '__main__':
    main()
