def sortlinks(linklist, unique_strings):
    for string in linklist:
        if string not in unique_strings:
            unique_strings.append(string)
    linklist[:] = unique_strings

links = ["hello", "bay", "hlleo", "hello", "olla", "olla", "bay"]
sortlinks(links)
print(links)