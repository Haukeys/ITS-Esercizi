def is_valid_ipv4(address: str) -> bool:
    
    parts:list[str] = address.split(".")

    
    if len(parts) != 4:
        return False

    for part in parts:
        
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False

        if part != str(int(part)):
            return False

    return True


print(is_valid_ipv4("192.168.0.1"))
print(is_valid_ipv4("255.255.255.255")) 
print(is_valid_ipv4("256.100.10.1") )
print(is_valid_ipv4("192.168.1") )
print(is_valid_ipv4("192.168.1.a"))