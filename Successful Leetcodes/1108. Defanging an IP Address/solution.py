def defangIPaddr(self, address: str) -> str:
    temp = []
    
    for c in address:
        if c == '.':
            temp.append('[.]')
        else:
            temp.append(c)
            
    return ''.join(temp)

# return address.replace('.', '[.]')

        