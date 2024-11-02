class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)  # Get the length of the sentence
        index = 0  # Initialize index to iterate through the sentence

        # Store the first character of the first word
        first_Character_of_First_Word_of_Sentence = sentence[0]
        # Store the last character of the last word
        last_Character_of_Last_Word_of_Sentence = sentence[-1]

        # Check if the first character of the first word matches the last character of the last word
        if first_Character_of_First_Word_of_Sentence != last_Character_of_Last_Word_of_Sentence:
            return False  # Return False if they do not match
        
        # Iterate through each character in the sentence
        while index < n:
            current_Character = sentence[index]

            # Check for spaces to identify word boundaries
            if current_Character == ' ':
                last_Character_of_Previous_Word = sentence[index - 1]  # Last character of the previous word
                first_Character_of_Next_Word = sentence[index + 1]  # First character of the next word

                # Check if the last character of the last word matches the first character of the next word
                if last_Character_of_Previous_Word != first_Character_of_Next_Word:
                    return False  # Return False if they do not match
            
            index += 1  # Move to the next character

        return True  # Return True if all checks pass