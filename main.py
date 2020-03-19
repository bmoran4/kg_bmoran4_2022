#!/usr/bin/env python3

import collections
import sys

# Functions

def false():
	print('false')
	sys.exit(0)

def check_length(str1, str2):
    if len(str1) > len(str2):
        false()

def check_mapping(str1, str2):
    mapping = {}
    element = int(0)
    
    for character in str1:
        if character in mapping.keys():
            if str2[element] != mapping[character]:
                false()
    else:
        mapping[character] = str2[element]
    element += 1

def main():
    
    #Check Input
    if len(sys.argv) != 3:
        print("Error: Wrong Number of Inputs)
        sys.exit(1)
        
	string1   = sys.argv[1]
	string2   = sys.argv[2]
    
	check_length(string1, string2)
	check_mapping(string1, string2)

	#All tests passed
	print('true')
    
# Main Execution

if __name__ == '__main__':
	main()
