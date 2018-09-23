#!/usr/bin/env python3

def main():
    nums = [int(input("Enter a number: ")) for i in range(3)]
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    print(max)

if __name__ == "__main__":
    main()
