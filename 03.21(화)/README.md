##
파일은 `임정_기둥과보` 와 같이 저장해주세요.


### 1. example test


### 2. varaible declearation

- answer: answer string 

ex) s: aabbaccc   -> 2a2ba3c

- compressed: unit string to compressed

- count: compressed unit string count

- prev: concat(count, compressed) will be part of answer

### 3. idea

- s's length is over 1 and below 1000, thus i will be ok with nested loop and  compeleted search

- len(compressed) will be 1 to len(s)//2 


