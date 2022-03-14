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
