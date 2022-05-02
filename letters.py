from lark import Lark
import sys
import re

def eval_tree(t):
    if t.data == "start":
        for x in t.children:
            eval_tree(x)
    elif t.data == "statement":
        #print("STATEMENT")
        eval_tree(t.children[0])
    elif t.data == "command":
        if t.children[0].data == "print":
            eval_print(t.children[1])
        elif t.children[0].data == "add":
            eval_add(t.children[1:])
        elif t.children[0].data == "char_print":
            eval_char_print(t.children[1:])


def eval_print(t):
    print(t.children[1].children[0])

def eval_char_print(t):
    out = ""
    for x in t:
        #print(x.data)
        if x.data == "arg":
            #print(x.children[1].children[0])
            out = out + x.children[1].children[0][0]
    print(out)

def eval_add(t):
    nums = []
    for x in t:
        if x.data == "arg":
            for y in x.children[1].children:
                if len(re.findall('[0-9]+',y)) == 1:
                    nums.append(re.findall('[0-9]+',y)[0])
    out = ""
    total = 0
    for x in nums:
        total = total+int(x)
        out = out + "+" + x
    print(out[1:] + "=" + str(total))


def main(argv):
    f = open("lettersGrammer.txt", "r")
    my_grammar = f.read()
    f.close()
    parser = Lark(my_grammar)
    f = open(argv, "r")
    program = f.read()
    f.close()

    parse_tree = parser.parse(program)
    eval_tree(parse_tree)

if __name__ == "__main__":
    main(sys.argv[1])
