class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        address = address.split(".")
        i = 0

        while i < len(address) - 1:
            result += address[i] + "[.]"
            i += 1

        return result + address[i]
        
