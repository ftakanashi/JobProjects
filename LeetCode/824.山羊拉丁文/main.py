#!/usr/bin/env python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        new = []
        for i, word in enumerate(words):
            if word[0].lower() in "aeiou":
                new_word = word + "ma" + "a" * (i + 1)
            else:
                new_word = word[1:] + word[0] + "ma" + "a" * (i + 1)
            new.append(new_word)
        return " ".join(new)