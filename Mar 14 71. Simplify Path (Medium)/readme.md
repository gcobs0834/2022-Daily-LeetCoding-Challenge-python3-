**[LeetCode Discuss Post](https://leetcode.com/problems/simplify-path/discuss/1847554/PythonGO-StackArray-Solution-and-Explanation)**
# [Python/GO] 🌟 Stack/Array Solution and Explanation 💕
## 1️⃣ Main Idea:
```A double period '..' refers to the directory up a level``` would definitely be a thing we need to solve. We can use stack to implement pop out to up a level

**Algo**
1. Make path split by "/" into pathList
2. Iterate through pathList
	 * If current directory == "" or directory =="."  We do noops continue to next directory
	 * If directory == "..", we have to pop out last member in stack, by doing this we can make path up a level
	 * If it's a directory, append it into stack
3. Iterate through stack and combine all directory into a output path

**Note** : We implement we call *stack* by array, So we can pop out last element and still can iterate from begining to the end.

## Complexity Analysis
* Time: O(N): Let N be the length of string
* Space: O(N): Iterate through path.split('/') take O(N) and Add up res in stack take O(N) => O(2N) = O(N)

## Code

**Python**
```python
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
```
**Go**
```go
func simplifyPath(path string) string {
    pathList := strings.Split(path, "/")
    dirList := make([]string, 0)
    
    for _ , dir := range pathList{
        // Ignore
        if dir == "" || dir == "."{
            continue
        }
        // Directory up a level
        if dir == ".."{
            if len(dirList) != 0{
                dirList = dirList[:len(dirList) - 1]
            }
        // Append it in dirList
        } else {
            dirList = append(dirList, dir)
        }
    }
    output := "/"
    // Make all dir in dirList add in res
    for _, dir := range dirList{
        output += dir
        output += "/"
    }
    // If res == "/" return it else pop out last string
    if output == "/"{
        return output
    }

    return output[:len(output) - 1]
}
```
* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
