import os
import sys


def main():
    # traditional way of creating a file
    f = open('my_file.txt', 'w') # make a file called 'my_file.txt' which is writeable, variable is f
    print(f)
    f.write('my name is PAUL')
    f.close() # traditional
    print(f) # the file is closed

    g = open('my_file.txt', 'r') # open for reading only
    text = g.read() # read everything
    # g.write('some text') # exception is raised because the file is read-only
    g.close()

    print(text)

    # modern way
    # context manager: automatically close the file once the context is exited
    with open('my_other_file.txt', 'w') as f:
        f.write('another interesting thing\n')
        print('the name of the day is Wednesday', file=f)
    # no need to close; once we exit the context the file is closed for us; best-practice

    # read in a context manager
    with open('my_other_file.txt') as g:
        print(g.readlines()) # reads the lines as a list of strings
    return os.EX_OK # constants


if __name__ == "__main__":  # guard in case you import this module
    sys.exit(main())
