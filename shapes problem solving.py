def lines(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + '#'

    return line_str

def square(n):
    square_str = ''
    for i in range(n):
        square_str += (line(n) + '\n')
    
    return square_str

def rectangle(width, height):
    rectangle_str = '' <== height because this needs to loop as long as it is.
    for i in range(height):
        rectangle_str = rectangle_str += (line(width) + '\n')
    
    return rectangle_str

reverse stairs
def space_line(spaces, hashes):
    return spaces * ' ' + hashes * '#'
    for level_len in range(n):
        stair_str += (space_line(n-level_len-1, level_len+1) + '\n')
