import cmd
import sys
from parser import parser

class Shell(cmd.Cmd):
    intro = 'Combine search module'
    prompt = 'Enter your query (quit to leave, ? for help): '
    file = None

    def do_parse(self, line):
        'Launch parser and search information are you interested for'
        information = parser(input('Enter your query: '))
        print('Searching...')
        print(information)
    def emptyline(self):
        pass
    def do_quit(self, line):
        'Turn off search module'
        print('Bye.')
        return True