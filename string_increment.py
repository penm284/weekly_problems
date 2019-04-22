def increment_string(strng):
    
    if strng != "":
        strlen = len(strng)
        
        for x in strng:
            if strng[strlen - 1].isdigit():
                strlen -= 1
        
        numbers = "".join([x for x in strng[strlen:]])
        letters = "".join([x for x in strng[:strlen]])
        
        zeros = 0

        for x in numbers:
            if x == "0":
                zeros += 1
            else:
                break

        if numbers == "":
            return letters + "1"
        elif zeros == len(numbers):
            numbers = int(numbers)
            increment = str(numbers + 1)
            return letters + (("0" * (zeros - 1)) + increment)
        else:
            numbers = int(numbers)
            increment = str(numbers + 1)
            if len(str(numbers)) < len(increment):
                return letters + (("0" * (zeros - 1)) + increment)
            else:
                return letters + (("0" * zeros) + increment)

    return "1"
