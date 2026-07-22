class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            # Format: <length>#<string>
            encoded_string += f"{len(string)}#{string}"
        return encoded_string

        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        
        while i < len(s):
            # 1. Find where the delimiter '#' is located
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. Extract the length (works even for multi-digit numbers like "12#")
            length = int(s[i:j])
            
            # 3. Slice out the exact word right after the '#'
            word = s[j + 1 : j + 1 + length]
            decoded_list.append(word)
            
            # 4. Jump pointer past the decoded word to start the next one
            i = j + 1 + length
            
        return decoded_list