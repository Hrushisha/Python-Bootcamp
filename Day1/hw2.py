#n=678432
#f=678
#s=432

def rearrange_number(n, f, s):
    n_str = str(n)
    
    first_part = n_str[:len(str(f))]
    second_part = n_str[-len(str(s)):]
    middle_part = n_str[len(str(f)):-len(str(s))]
    
    rearranged = second_part + first_part + middle_part
    return rearranged

# Example usage
n = 678432
f = 678
s = 432
output = rearrange_number(n, f, s)
print(f"Output: {output}")