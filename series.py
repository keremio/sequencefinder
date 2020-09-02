s = input()
c_a = 0
c_g = 0
gn_a = 0
gn_g = 0
inv_a = 0
inv_g = 0
array = list(map(int, s.split()))
for i in range (2, len(array)):
    if (array[i] - array[i-1] == array[i-1] - array[i-2]): 'checking if the sequence is an arithmetic sequence
        c_a += 1
    if (array[i] / array[i-1] == array[i-1] / array[i-2]): 'checking if the sequence is a geometric sequence
        c_g += 1

if (c_a == len(array) - 2 and c_g == len(array) - 2): 'if a sequence is both arithmetic and geometric, it is constant.
    print("this is a constant sequence\n")
elif (c_g == len(array) - 2):
    gn_g = array[1] / array[0] 'evaluating the general rule of a geometric sequence
    inv_g = array[0] / gn_g
    print("this is a geometric sequence\n")
    print("the general rule of this sequence is " + str(gn_g) + "^n * " + str(inv_g)) 
elif (c_a == len(array) - 2):
    print("this is an arithmetic sequence\n") 'evaluating the general rule of an arithmetic sequence
    gn_a = array[1] - array[0]
    inv_a = array[0] - gn_a
    print("the general rule of this sequence is " + str(int(gn_a)) + "n +" + str(int(inv_a))) 
else:
    print("this is not a sequence")

