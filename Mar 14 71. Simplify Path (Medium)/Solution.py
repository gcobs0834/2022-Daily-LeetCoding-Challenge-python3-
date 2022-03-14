class Solution:
    def simplifyPath(self, path: str) -> str:
        dirList = []
        
        for directory in path.split('/') :
            # Ignore
            if not directory or directory == ".":
                continue
            # Directory up a level
            if directory == "..":
                if dirList:
                    dirList.pop()
            # Append it in dirList
            else:
                dirList.append(directory)
                
        res = "/"
        # Make all dir in dirList add in res
        for directory in dirList:
            res += directory
            res += "/"
        # If res == "/" return it else pop out last string
        return res[:-1] if res != "/" else "/"
