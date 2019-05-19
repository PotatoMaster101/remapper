# Remapper
Remaps the input string to random characters. 

# Usage
Run with python 3. 
```bash
$ python3 remapper.py [-h] [-v] [-p POOL] [-a] [-n] [-aL] [-aU] [-i IGNORE] [-iP]
                      [-iN] [-e ERRCHAR] [-l HINTS [HINTS ...]]
                      input
```

# Example
Basic usage:
```
$ python3 remapper.py "remap this string"
xkJ+9f2^~&f&2x~vY
```

Verbose output:
```
$ python3 remapper.py "remap this string" -v
[+] Map:      {'r': ']', 'e': 'i', 'm': 'd', 'a': '3', 'p': '%', ' ': '{', 't': 'r', 'h': 'v', 'i': '[', 's': 'n', 'n': 'y', 'g': 'G'}
[+] Original: remap this string
[+] Pool:     ?DNG&6i2S`ad~JnM\VX,>!4/]O^Fu-%qr$v5BUeELA}|Thx[gs;mpw+bzK(@*CjRIc97YfP=HtQ#{3Zkl)_W:<1o'"08.y
[+] Ignored:  
[+] Hints:    []
[+] Output:   ]id3%{rv[n{nr][yG
```

Specify custom character pool:
```
$ python3 remapper.py "remap this string" -v -p abcde1234567
[+] Map:      {'r': 'e', 'e': 'd', 'm': '3', 'a': '7', 'p': 'a', ' ': '6', 't': 'b', 'h': '5', 'i': '2', 's': '1', 'n': '4', 'g': 'c'}
[+] Original: remap this string
[+] Pool:     c6d2a175be43
[+] Ignored:
[+] Hints:    []
[+] Output:   ed37a6b52161be24c
```

Ignore specified characters: 
```
$ python3 remapper.py "remap this string!" -v -i remap!
[+] Map:      {'r': 'r', 'e': 'e', 'm': 'm', 'a': 'a', 'p': 'p', '!': '!', ' ': 'Q', 't': '=', 'h': '|', 'i': '{', 's': 'z', 'n': '4', 'g': 'c'}
[+] Original: remap this string!
[+] Pool:     l/zy}xR[&sP1L4(0buc~;7C-w{Eg5'*Jk="9,@Fh_nY?U3tiGoSq)<TWBKfVZQdO:#X2%H>8vj^.\6M`I]A|N+D$
[+] Ignored:  remap!
[+] Hints:    []
[+] Output:   remapQ=|{zQz=r{4c!
```

Only map to lowercase letters and brackets:
```
$ python3 remapper.py "remap this string!" -v -a -p "{}()<>"
[+] Map:      {'r': 'j', 'e': 'w', 'm': 'e', 'a': 'b', 'p': 'm', ' ': 'l', 't': 'r', 'h': 'o', 'i': 'y', 's': 'k', 'n': '{', 'g': 'p', '!': 'd'}
[+] Original: remap this string!
[+] Pool:     fe}qt<bcrwxpdsz{>iolgamjhuk(n)vy
[+] Ignored:  
[+] Hints:    []
[+] Output:   jwebmlroyklkrjy{pd
```

Specify predefined mappings:
```
$ python3 remapper.py "remap this string!" -v -l remap=ABCDE
[+] Map:      {'r': 'A', 'A': 'r', 'e': 'B', 'B': 'e', 'm': 'C', 'C': 'm', 'a': 'D', 'D': 'a', 'p': 'E', 'E': 'p', ' ': '<', 't': 'z', 'h': 'l', 'i': '&', 's': '.', 'n': '*', 'g': 'M', '!': 't'}
[+] Original: remap this string!
[+] Pool:     38hA(70jZ`xYy1dk*u5T\#z_BmK:DNs.tQ;g[@9oX-El'v~,G<}W+Lq|nJaV$^6c)eRwf2M"HOIC?i]{p&U4b>/S%F!P=r
[+] Ignored:
[+] Hints:    ['remap=ABCDE']
[+] Output:   ABCDE<zl&.<.zA&*Mt
```

Custom error string when character pool is exhausted:
```
$ python3 remapper.py "abcdefgh" -v -p abc -e "<char empty>"
[+] Map:      {'a': 'a', 'b': 'c', 'c': 'b', 'd': '<char empty>', 'e': '<char empty>', 'f': '<char empty>', 'g': '<char empty>', 'h': '<char empty>'}
[+] Original: abcdefgh
[+] Pool:     acb
[+] Ignored:  
[+] Hints:    []
[+] Output:   acb<char empty><char empty><char empty><char empty><char empty>
```

