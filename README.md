# Coding_Challenge

The program simulates the creation of subdirectories (folders) for an OS. The input file to your program, input.dat, will contain a
sequence of commands that a user might enter from a command line, and the output file file.out will contain the
operating system’s responses to these commands.

## Usage 

```"Usage: python console.py [command file] > [output file]"```

## Sample input

```
dir
mkdir sub6
mkdir sub3
mkdir sub4
dir
mkdir sub4
cd sub3
cd sub3
mkdir sub3
mkdir sub6
mkdir sub4
dir
cd sub6
dir
cd sub6
mkdir sub666
dir
up
up
dir
up
```

## Sample Output

``` 
Directory Problem by Mike
Command: dir
Directory of root:
No subdirectories
Command: mkdir sub6
Command: mkdir sub3
Command: mkdir sub4
Command: dir
Directory of root:
sub3 sub4 sub6
Command: mkdir sub4
Subdirectory already exists
Command: cd sub3
Subdirectory does not exist
Command: cd sub3
Command: mkdir sub3
Command: mkdir sub6
Command: mkdir sub4
Command: dir
Directory of root\sub3:
sub3 sub4 sub6
Command: cd sub6
Subdirectory does not exist
Command: dir
Directory of root\sub3\sub6:
No subdirectories
Command: cd sub6
Command: mkdir sub666
Command: dir
Directory of root\sub3\sub6:
sub666
Command: up
Command: up
Command: dir
Directory of root:
sub3 sub4 sub6
Command: up
Cannot move up from root directory
End of Directory Problem by Mike
```

## Things I didn't get to:

- Adding StdIn input
- More error handling with more verbose outputs
- Automated tests
- Not using print for output.  Wanted to write into file but didn't have time to switch.  
