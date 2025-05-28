class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_words = []
        cur_len = 0 

        for w in words:
            if cur_len + len(cur_words) + len(w) > maxWidth:
                total_spaces = maxWidth - cur_len
                gaps = len(cur_words) - 1

                if gaps == 0:
                    line = cur_words[0] + " " * total_spaces
                else:
                    even = total_spaces // gaps
                    extra = total_spaces % gaps
                    parts = []
                    for i, word in enumerate(cur_words[:-1]):
                        spaces = even + (1 if i < extra else 0)
                        parts.append(word + " " * spaces)
                    parts.append(cur_words[-1]) 
                    line = "".join(parts)

                res.append(line)

                cur_words = [w]
                cur_len = len(w)
            else:
                cur_words.append(w)
                cur_len += len(w)

        last_line = " ".join(cur_words)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)

        return res
