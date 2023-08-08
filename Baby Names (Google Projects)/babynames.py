#!/usr/bin/python
import sys
import re

"""
Baby Names exercise
Given a file name for baby.html, returns a list starting with the year string
followed by the name-rank strings in alphabetical order.
['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
"""


def extract_names(filename):
 
  with open(filename, 'r') as file: #opening file using 'with'
    text = file.read() #reads and stores data in a new variable

  result = [] #stores resulting list
  year = (re.search(r'baby(\w+).html', filename)).group(1) #searching for year in the filename

  for line in text.split('\n'): #splitting text on the basis of newline

    match = re.search(r'<tr align="right"><td>(\w+)</td><td>(\w+)</td><td>(\w+)</td>', line) #searching for m/f name and rank
    if match:
      result.append(f'{match.group(2)} {match.group(1)}') #male_name:rank
      result.append(f'{match.group(3)} {match.group(1)}') #female_name:rank
  
  result.insert(0, year) #inserts year at start after converting to str
  result.sort() #sorts alphabetically

  with open(f'result_{year}.txt', 'w') as file: #creates a .txt file (eg: result2006.txt)
    
    for value in result: #stores individual values of result on a newline in .txt file
      file.write(f'{value}\n')
  
  return f'result_{year}.txt created' #returns a text stating the name of file created


def main():

  args = sys.argv[2:] #removing .py filename and file from args (args = [.py filename, file, .html filename])
  
  if args: #if args are provided, else print the format in which args are to be provided
    print(extract_names(args[0])) #args = [.html filename]
  else:
    print ('usage:[name of python program] file [file ...]') #eg: python3 babynames.py file baby2006.html
    sys.exit(1) #ending code execution

  
if __name__ == '__main__':
  main()