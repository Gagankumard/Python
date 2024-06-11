# find largest num

def find_max(number):
    max=number[0]
    for numbers in number:
        if numbers>max:
            max=numbers 
    return max