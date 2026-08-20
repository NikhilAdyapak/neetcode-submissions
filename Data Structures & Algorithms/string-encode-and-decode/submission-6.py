class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            if s == "":
                out += "#"
            else:
                out += str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        indx = 0
        while indx < len(s):

            if s[indx] == "#":
                out.append("")
                indx += 1
            else:
                length = ""
                while(s[indx] != "#"):
                    length += s[indx]
                    indx += 1
                l = int(length)
                out.append(s[indx + 1: indx + 1 + l])
                indx += 1 + l

        return out
