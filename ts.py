import sys

COMMANDS = ['cd', 'dir', 'mkdir', 'up']

class Directory(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.directories = []

    def add_sub(self, sub):
        """ add new sub directory """
        self.directories.append(sub)

class Console(object):
    def __init__(self, out):
        self.root = Directory('/', None)
        self.cur_directory = self.root
        self.out = out

    def dir(self):
        """Print current directory and it's subidrectories."""

        dir_name = '\\'
        cur_directory = self.cur_directory

        ## Find Current directory path
        while 1:
            if cur_directory.parent == None:
                break
            dir_name = '\\' + cur_directory.name + dir_name
            cur_directory = cur_directory.parent

        if dir_name == '\\':
            dir_name = 'root'
        else:
            dir_name = 'root' + dir_name
            dir_name = dir_name[0:-1] + ':'
        print('Directory of %s' % dir_name)

        ## Print subdirectories
        if not self.cur_directory.directories:
            print('No subdirectories')
        else:
            for x in self.cur_directory.directories:
                print(x.name)

    def up(self):
        """Go up one level in directory"""
        if self.cur_directory.parent == None:
            print('Cannot move up from root directory')
        self.cur_directory = self.cur_directory.parent

    def mkdir(self, name):
        """ Make a new directory """
        ## post error if duplicate directory exists, otherwise add directory
        for subs in self.cur_directory.directories:
            if subs.name == name:
                print('Subdirectory already exists')
                return

        ## Save new path name
        # new_name = self.cur_directory.name + name + '/'
        new_dir = Directory(name, self.cur_directory)
        self.cur_directory.add_sub(new_dir)

    def cd(self, name):
        """ Change to a different directory """
        for sub_dir in self.cur_directory.directories:
            if sub_dir.name == name:
                self.cur_directory = sub_dir
                return
            else:
                print('Subdirectory does not exist')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python console.py [command file] [output file]"
        exit()
    infile = open(sys.argv[1], 'r')
    out = open(sys.argv[2], 'w+')
    commands = infile.readlines()
    console = Console(out)
    print("Directory Problem by Mike")
    for command in commands:
        tokens = command.split()
        if tokens[0] not in COMMANDS:
             print('Command does not exist\n') ##TO DO
        else:
            if tokens[0] == 'dir':
                print("Command: dir")
                console.dir()
            elif tokens[0] == 'mkdir':
                print("Command: %s %s") % (tokens[0], tokens[1])
                console.mkdir(tokens[1])
            elif tokens[0] == 'up':
                print("Command: up")
                console.up()
            else:
                print("Command: %s %s") % (tokens[0], tokens[1])
                console.cd(tokens[1])
    print("End of Directory Problem by Mike")
