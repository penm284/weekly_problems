#new function input is ohms
def color(ohms):
#arr of resistor colors
    colors = ['black','black','black','gold']
#making list
    arr = list(ohms)
#iterating through index values 1-6 of arr
    for i in range(1,6):
#deletes last 6 elements of arr
        arr.pop(-1)

#new variables
    pos = 0
    mul = 0
#finding multiple of each color
    for i in range(len(arr)):
        if arr[pos] == '0':
            colors[pos] = 'black'
            mul = mul + 1
        elif arr[pos] == '1':
            colors[pos] = 'brown'
            mul = mul + 1
        elif arr[pos] == '2':
            colors[pos] = 'red'
            mul = mul + 1
        elif arr[pos] == '3':
            colors[pos] = 'orange'
            mul = mul + 1
        elif arr[pos] == '4':
            colors[pos] = 'yellow'
            mul = mul + 1
        elif arr[pos] == '5':
            colors[pos] = 'green'
            mul = mul + 1
        elif arr[pos] == '6':
            colors[pos] = 'blue'
            mul = mul + 1
        elif arr[pos] == '7':
            colors[pos] = 'violet'
            mul = mul + 1
        elif arr[pos] == '8':
            colors[pos] = 'gray'
            mul = mul + 1
        elif arr[pos] == '9':
            colors[pos] = 'white'
        elif arr[pos] == 'k':
            mul = mul + 3
        elif arr[pos] == 'M':
            mul = mul + 6
        pos = pos + 1
#subtracting 2 from mul to account for extra digits
    mul = mul - 2
    if mul == 0:
        colors[2]= 'black'
    if mul == 1:
        colors[2]= 'brown'
    if mul == 2:
        colors[2]= 'red'
    if mul == 3:
        colors[2]= 'orange'
    if mul == 4:
        colors[2]= 'yellow'
    if mul == 5:
        colors[2]= 'green'
    if mul == 6:
        colors[2]= 'blue'
    if mul == 7:
        colors[2]= 'violet'
    if mul == 8:
        colors[2]= 'gray'
    if mul == 9:
        colors[2]= 'white'

    print(colors)

#running test cases
def run():
    color("10 ohms")
    color("100 ohms")
    color("220 ohms")
    color("330 ohms")
    color("470 ohms")
    color("680 ohms")
    color("1k ohms")
    color("10k ohms")
    color("22k ohms")
    color("47k ohms")
    color("100k ohms")
    color("330k ohms")
    color("2M ohms")

run()
