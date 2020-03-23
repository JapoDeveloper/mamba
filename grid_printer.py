CELL_LENGTH = 4 

def ncall(func,n,*args,**kvargs):
    """
        Helper to execute a function several times
        Example:
            ncall(print,2,'Hello World!')
    """
    for _ in range(n):
        func(*args,**kvargs)

def print_plus():
    print('+', end=' ')

def print_dash():
    print('-', end=' ')

def print_bar():
    print('|', end=' ')

def print_space():
    print(' ', end=' ')

def print_end():
    print()

def print_plus_sequence(ncol):
    """
        Print a sequence of '+' and '-' separated with spaces and finishing with a '+'
        Example:
            + - - - - + - - - - +
    """
    for _ in range(ncol):
        print_plus()
        ncall(print_dash, CELL_LENGTH)
    print_plus()
    print_end()

def print_bar_sequence(ncol):
    """
        Print a sequence of '|' separated with spaces
        Example:
            |         |         |
    """
    for _ in range(ncol):
        print_bar()
        ncall(print_space, CELL_LENGTH)
    print_bar()
    print_end()
    
def print_row(ncol):
    # Head
    print_plus_sequence(ncol) 
    # Body
    ncall(print_bar_sequence, CELL_LENGTH, ncol)

def draw_grid(nrows, ncolumns):
    ncall(print_row, nrows, ncolumns)
    print_plus_sequence(ncolumns)

if __name__ == '__main__':
    draw_grid(3,5)  
