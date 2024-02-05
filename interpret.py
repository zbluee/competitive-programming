class Solution:

    def interpret(self, command: str) -> str:
        buf = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                buf += "G"
            elif command[i] == "(" :
                if i < len(command) and command[i + 1] == ")":
                    buf += "o"
                    i += 1
                elif i < len(command) and command[i + 1] == "a":
                    buf += "al"
                    i += 2
            i += 1

        return buf

        
        
