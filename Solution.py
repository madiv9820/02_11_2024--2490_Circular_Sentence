class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the input sentence into words
        words = sentence.split()
        n = len(words)  # Get the number of words in the sentence

        # Check each pair of consecutive words
        for index in range(n-1):
            current_Word = words[index]  # Current word in the iteration
            next_Word = words[index+1]    # Next word to compare with

            # Check if the last character of the current word
            # matches the first character of the next word
            if current_Word[-1] != next_Word[0]:
                return False  # Return False if they don't match
        
        # After checking all consecutive pairs, check the first and last words
        first_Word, last_Word = words[0], words[-1]
        # Check if the first character of the first word
        # matches the last character of the last word
        if first_Word[0] != last_Word[-1]:
            return False  # Return False if they don't match
        
        # If all checks pass, return True indicating it's a circular sentence
        return True