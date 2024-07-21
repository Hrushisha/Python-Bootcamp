#n=123456
#f=123
#s=45
#output:54123


def rearrange_number(n, f, s):
    n_str = str(n)
    
    first_part = n_str[:f]
    second_part = n_str[-s:]
    middle_part = n_str[f:-s]
    
    rearranged = second_part + first_part + middle_part
    return rearranged


n = 123456
f = 3
s = 2
output = rearrange_number(n, f, s)
print(f"Output: {output}")