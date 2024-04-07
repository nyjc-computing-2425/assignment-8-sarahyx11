# Built-in imports
def reverse(text):
    '''
    function takes in text and reverses it
    parameter:
    string: text 
    returns:
    string: reversed text
    '''
    if len(text) == 0:
        return ''
    else:
        return reverse(text[1:]) + text[0]

def is_palindrome(text):
    '''
    takes in text and checks if its a valid palindrome
    palindrome is a sentence or number with a sequence of letters, such that it reads the same way forwards and backwards.
    parameters:
    string: text
    returns:
    Boolean: True if text is a palindrome and False if text is not a palindrome
    '''
    text = text.lower()
    text = text.strip()
    clean_text = ""
    for letter in text:
        if letter.isalnum():
            clean_text += letter
          
    if len(clean_text) > 1:
      if clean_text[0] == clean_text[-1]:
        return is_palindrome(clean_text[1:-1])
      else:
        return False
    elif len(clean_text) <= 1:
      return True
    else:
      return False

