import glob

#get file name
list_of_file = glob.glob("*.mx3")
print(list_of_file)
result = []
#repulicated with different B in new file
for i in list_of_file:
    with open(i) as file:
        a = file.readlines()
        print(a)
        #last element, len(a) - 1
        ext = a[42]
        number = ext.split(",")
        number_to_chagne = int(number[0][18])

        
        for i in range(10):
            if i > number_to_chagne:
                result.append(i)
        
        
        for b in result:
            with open(f"0.{b}.mx3", "w") as file2:
                for line in a:
                    if "B_ext" in line:
                        file2.write(f"B_ext = vector(0.0{b}, 0, 0)\n")
                    else:
                        file2.write(line)
        
