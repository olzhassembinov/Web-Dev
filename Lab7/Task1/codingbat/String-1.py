#combo string
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return  a + b + a      

#non start
def non_start(a, b):
    return a[1:] + b[1:]

#make abba
def make_abba(a, b):
    return a + b + b + a

#make tags
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

#make out word
def make_out_word(out, word):
    return out[:2] + word + out[2:]

#extra end
def extra_end(str):
    return str[-2:] * 3

#first two
def first_two(str):
    return str[:2]

#first half
def first_half(str):
    return str[:len(str)/2]

#without end
def without_end(str):
    return str[1:-1]

#hello name
def hello_name(name):
    return "Hello " + name + "!"

#left2
def left2(str):
    return str[2:] + str[:2]

