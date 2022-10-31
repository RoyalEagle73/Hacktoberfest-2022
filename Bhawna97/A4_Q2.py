def powe_of_two(N):
    if(N == 0):
        return 0;
    while (N != 1):
        if (N %2 != 0 and N != 1):
            return 0;
        N = N // 2
    return 1;

print(powe_of_two(128))
print(powe_of_two(150))
