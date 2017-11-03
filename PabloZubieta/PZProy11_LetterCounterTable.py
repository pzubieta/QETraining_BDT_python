def lettersTable(strWord, char):
    count = 0
    while count <= len(strWord):
        for char in word:
            if char == strWord[count]:
                count += 1
            return count

def count_letters(word, char):
  return sum(char == c for c in word)

print lettersTable('banana','a')

