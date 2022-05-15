# import regular expression re
import re 
# declare path of input and output files as strings
input_file = "Second Part/Input/input.txt"
output_file = "Second Part/Output/output.txt"

# define reader() function
def reader():
    # declare empty list word_list 
    word_list = []
    # open input file in read mode as f
    with open(input_file,'r') as f:
        # for each line in f
        for line in f:
            # trim line using .strip() method
            trimmed_line = line.strip()
            # use re.split() function to split line by , . ? ; characters
            words = re.split("\s|[,.?;]",trimmed_line)
            # for each splitted word in words:
            for word in words:
                # if it is not empty string append to word_list
                if word != "":
                    # append lower case of word to word_list
                    word_list.append(word.lower())
    # call to transformation function with word_list  as argument
    transformation(word_list)

# define transformation() which take word_list 
def transformation(word_list):
    # convert given word_list to set word_set
    word_set = set(word_list)
    # create empty dictionary word_list
    word_dict = dict()
    # for each word in word_set
    for word in word_set:
        # assign count of word in word_list to value for key = word in dictionary
        word_dict[word] = word_list.count(word)
    
    # call to writer() function with word_dict as argument
    writer(word_dict)

# define writer method
def writer(word_list):
    # open output file in write mode as f
    with open(output_file,'w') as f:
        # for key=word,value=count in word_dict dictionary
        for word,count in word_list.items():
            # writer this f string "word -> count for that word"
            f.write(f"{word} -> {count}\n")

# driver code
def main():
    reader()

# string point
if __name__ == "__main__":
    main()
