
"""
Randy and Latif, I very much appreciated the chance to speak with you
yesterday. I also enjoyed the problem. This is it, with some comments:

I added the condition that the length arg has to be greater than the
length of the longest words in the sentence; interestingly in the
example provided in the comments, the length of 10 returns the word
"destination.", which has a length of 12. I took the liberty of
changing this. Without it a solution is admittedly more concise.

The logic was a bit tricky... I found it necessary to use a break
statement, which I went to some lengths to avoid before accepting it.
It seemed un-'pythonic' to me initially, but without it I was getting 
an index out of range error in the nested while clause.
"""

def split_words(sentence, length):
    l_words = sentence.split()
    l_lengths = [len(wrd) for wrd in l_words]

    if max(l_lengths) < length:
        l_out = []

        while len(l_words) >= 1:
            subs = ''
            while len(subs + l_words[0] + '-') <= length:
                subs += f'{l_words[0]}-'
                l_words.pop(0)
                if len(l_words) == 0:
                    break
            if subs != '': l_out.append(subs)
        
        # remove '-' from ends of substrings 
        l_out = [s[:len(s)-1] if s.endswith('-') else s for s in l_out]
        return l_out
    else:
        print('length value must be > length of longest word in sentence.')


# Function calls from bottom of problem
sentence1 = "The tall and shy boy likes to jump up and down for fun."
print(split_words(sentence1, 11))
print(split_words(sentence1, 8))
print(split_words(sentence1, 20))
print(split_words(sentence1, 2)) # returns length msg

# Example from problem comments
sentence2 = "A slim man ran for many miles to reach a distant destination."
print(split_words(sentence2, 10)) # returns length msg
print(split_words(sentence2, 18))
