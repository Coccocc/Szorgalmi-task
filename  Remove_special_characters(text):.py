# Author: Hegyi Dáneil 
# Neptune code: CJC6AN
# Email: rekellemail5@gmail.com
# Created: 2023-10-26
# Last Modified: 2023-10-27




def remove_special_characters(text):
    plain_text = ""
    
    for char in text:
        if char.isalnum() or char.isspace():
            plain_text += char
    
    return plain_text

text = "A kolbász,,, és a mariska!! pipacs??"
plain_text = remove_special_characters(text)
print(plain_text)
