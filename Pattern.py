# Full Pyramid of Stars 
#              * 
#             * * 
#            * * * 
#           * * * * 
#          * * * * * 
#           * * * * 
#            * * * 
#             * * 
#              *

def full_pyramid(n):
    print("\nFull Pyramid of Stars")
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

#..................................................................................................................


# Inverted Pyramid of Stars

#          * * * * * 
#           * * * * 
#            * * * 
#             * * 
#              *

def inverted_pyramid(n):
    print("\nInverted Pyramid of Stars")
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '* ' * i)
        
#..................................................................................................................

# Right-Angled Triangle

#     * 
#     * * 
#     * * * 
#     * * * * 
#     * * * * *

def right_angled_triangle(n):
    print("\nRight-Angled Triangle of Stars")
    for i in range(1, n + 1):
        print('* ' * i)
        
#..................................................................................................................


# Inverted Right-Angled Triangle

#     * * * * * 
#     * * * * 
#     * * * 
#     * * 
#     *

def inverted_right_angled_triangle(n):
    print("\nInverted Right-Angled Triangle of Stars")
    for i in range(n, 0, -1):
        print('* ' * i)
        
#..................................................................................................................


# Diamond Pattern

#              * 
#             * * 
#            * * * 
#           * * * * 
#          * * * * * 
#           * * * * 
#            * * * 
#             * * 
#              *

def diamond(n):
    print("\nDiamond Pattern")
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' * i)
        
#..................................................................................................................


# Hollow Square

#

def hollow_square(n):
    print("\nHollow Square Pattern")
    for i in range(n):
        if i == 0 or i == n - 1:
            print('* ' * n)
        else:
            print('* ' + '  ' * (n - 2) + '*')

#..................................................................................................................

# Number Pyramid
#
#
#
#
#
#
#
#
#
#
#

def number_pyramid(n):
    print("\nNumber Pyramid")
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


#..................................................................................................................

# Pascal’s Triangle
#
#
#
#
#
#
#
#
#
#
#

def pascals_triangle(n):
    print("\nPascal's Triangle")
    prev = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev[j - 1] + prev[j]
        print(' ' * (n - i), end='')
        print(' '.join(map(str, row)))
        prev = row

#..................................................................................................................


# Set n value
n = 5

# Call the functions with n
full_pyramid(n)
inverted_pyramid(n)
right_angled_triangle(n)
inverted_right_angled_triangle(n)
diamond(n)
hollow_square(n)
number_pyramid(n)
pascals_triangle(n)

#..................................................................................................................










