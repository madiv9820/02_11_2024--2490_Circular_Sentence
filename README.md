# Validate Circular Sentence

- ### Intuition
    -   A circular sentence is defined as one where:
        - The last character of each word matches the first character of the next word.
        - The first character of the first word matches the last character of the last word.

        The goal is to ensure that all transitions between words are valid, including the transition from the last word back to the first word.

- ### Approach

    1. **Split the Sentence**: Use the `split()` method to divide the input sentence into individual words, resulting in a list of words.

    2. **Check Consecutive Words**: Iterate through the list of words and:
        - Compare the last character of the current word with the first character of the next word.
        - If any pair does not match, return `False`.

    3. **Check the First and Last Word**: After checking all consecutive pairs, compare:
        - The first character of the first word with the last character of the last word.
        - If they do not match, return `False`.

    4. **Return True**: If all checks pass, return `True`, indicating the sentence is circular.

- ### Time Complexity

    - **Splitting the Sentence**: The `split()` operation takes \(O(m)\), where \(m\) is the length of the sentence.
    - **Checking Words**: The loop runs \(n-1\) times (where \(n\) is the number of words), with each check taking \(O(1)\).

        Overall, the time complexity is __\(O(m)\)__.

- ### Space Complexity

    - The space used by the `split()` function results in a list of words, requiring \(O(n)\) space (where \(n\) is the number of words).
    - Other variables take constant space.

        Thus, the space complexity is __\(O(n)\)__.

- ### Code
    ```python3 []
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
    ```