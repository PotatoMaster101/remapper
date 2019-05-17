# Remapper
Remaps the input string to random characters. 

# Usage
Run with python 3. 
```bash
$ python3 remapper.py [-h] [-v] [-p POOL] [-i IGNORE] [-e ERRCHAR]
                      [-l HINTS [HINTS ...]]
                      input
```

# Example
```bash
$ python3 remapper.py "abcdef abcdef"
5o<gt6%5o<gt6
```

Ignored characters: 
```bash
$ python3 remapper.py "PotatoMaster101" -i "Potato"
Potato$ajtx0FTF
```

Premapped characters: 
```bash
$ python3 remapper.py abcdef -l abc=xyz -v
[+] Map:      {'a': 'x', 'x': 'a', 'b': 'y', 'y': 'b', 'c': 'z', 'z': 'c', 'd': '}', 'e': '&', 'f': 'G'}
[+] Original: abcdef
[+] Ignored:
[+] Hints:    ['abc=xyz']
[+] Output:   xyz}&G
```

