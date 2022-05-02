from lark import Lark
import sys
import re


def eval_tree(t,offset=0):
    if t.data == "start":
        for x in t.children:
            if x.data == "offset_up":
                offset = offset + 1
            elif x.data == "offset_down":
                offset = offset - 1
            eval_tree(x, offset)
    elif t.data == "statement":
        eval_tree(t.children[0], offset)
    elif t.data == "command":
        if t.children[0].data == "print":
            eval_print(t.children[1:], offset)
        elif t.children[0].data == "add":
            eval_add(t.children[1:])
        elif t.children[0].data == "char_print":
            eval_char_print(t.children[1:], offset)


def eval_print(t,offset):
    for x in t:
        if x.data == "arg":
            print(x.children[1].children[offset])

def eval_char_print(t,offset):
    out = ""
    for x in t:
        if x.data == "arg":
            out = out + x.children[1].children[offset][0]
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
