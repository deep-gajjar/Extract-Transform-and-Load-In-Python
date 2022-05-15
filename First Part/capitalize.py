# declare path of input and output files as strings
input_file = "First Part/Input/input.txt"
output_file = "First Part/Output/output.txt"

# define reader() function
def reader():
    # declare empty list line_list
    line_list = []
    # open() input file in read mode as f
    with open(input_file, 'r') as f:
        # for each line in f
        for line in f:
            # append line to line_list    
            line_list.append(line)
    # call to transformation() function with line_list as arguments
    transformation(line_list)
    
# define transformation() function that will convert all letter of input to upper case
def transformation(line_list):
    # delcare size of list
    n = len(line_list)
    # for each line index
    for i in range(n):
        # update old line string with new one which is return by .upper() of string method
        line_list[i] = line_list[i].upper()
    
    # call to writer function with line_list as arguments
    writer(line_list)

# define writer() function that will write all line to output file
def writer(line_list):
    # open output file in write mode as f
    with open(output_file,'w') as f:
        # for each line in line_list write line to output file 
        for line in line_list:
            f.write(line)

# driver code
def main():
    reader()

# starting point
if __name__ == "__main__":
    main()
