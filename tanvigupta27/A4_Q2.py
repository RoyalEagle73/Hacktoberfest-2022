
Input1 = 128
Input2 = 140

def poweOfTwo(Input):
    if(Input == 0):
        return 0;
    while (Input != 1):
        if (Input %2 != 0 and Input != 1):
            return 0;
        Input = Input // 2
    return 1;

print(poweOfTwo(Input1))
print(poweOfTwo(Input2))
