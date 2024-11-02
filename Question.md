# 2490. Circular Sentence

__Type:__ Easy <br>
__Topics:__ String <br>
__LeetCode Link:__ [Circular Sentence](https://leetcode.com/problems/circular-sentence)
<hr>

A __sentence__ is a list of words that are separated by a __single__ space with no leading or trailing spaces.

- For example, `"Hello World"`, `"HELLO"`, `"hello world hello world"` are all sentences.

Words consist of __only__ uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is __circular__ if:

- The last character of a word is equal to the first character of the next word.
- The last character of the last word is equal to the first character of the first word.

For example, `"leetcode exercises sound delightful"`, `"eetcode"`, `"leetcode eats soul"` are all circular sentences. However, `"Leetcode is cool"`, `"happy Leetcode"`, `"Leetcode"` and `"I like Leetcode"` are not circular sentences.

Given a string `sentence`, return `true` _if it is circular_. Otherwise, return `false`.
<hr>

### Examples

- __Example 1:__ <br>
__Input:__ sentence = "leetcode exercises sound delightful" <br>
__Output:__ true <br>
__Explanation:__ The words in sentence are ["leetcode", "exercises", "sound", "delightful"]. <br> - leetcode's last character is equal to exercises's first character. <br> - exercises's last character is equal to sound's first character. <br> - sound's last character is equal to delightful's first character. <br> - delightful's last character is equal to leetcode's first character. <br> The sentence is circular.

- __Example 2:__ <br>
__Input:__ sentence = "eetcode" <br>
__Output:__ true <br>
__Explanation:__ The words in sentence are ["eetcode"]. <br> - eetcode's last character is equal to eetcode's first character.<br> The sentence is circular.

__Example 3:__ <br>
__Input:__ sentence = "Leetcode is cool" <br>
__Output:__ false <br>
__Explanation:__ The words in sentence are ["Leetcode", "is", "cool"]. <br> - Leetcode's last character is not equal to is's first character. <br> The sentence is not circular.

### Constraints:
- `1 <= sentence.length <= 500`
- `sentence` consist of only lowercase and uppercase English letters and spaces.
- The words in `sentence` are separated by a single space.
- There are no leading or trailing spaces.

### Hints
- Check the character before the empty space and the character after the empty space.
- Check the first character and the last character of the sentence.