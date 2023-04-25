#Gọi module openai
import openai
import os

openai.organization = 'org-AjTmCQ65Mt7m97gU3ZB8Gw6k'
openai.api_key = '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'

##############################################
# Training AI
# Đây là nơi train AI, hoặc cài prompt.



# set role
def set_role(level,standard):
    role = f'Jessica, the girl who is really bad in English. Can you help her to change her words to the level IELTS {level} by this {standard}.'
    return role

# set level
def set_level():
    level = input('What level do want to change(IELTS \n A:4.0 \n B:4.0-5.0 \n C:5.0-6.5 \n D:6.5-7.5 \n E:8.0\n Choose: ')
    return level

# set shot
def set_shot(level):   
    shot = f'you will check my writing test, and you will change my writing test to level {level}'
    return shot

# set text
def set_text():
    text = input('Input your text: ')
    return text
# data reference

#main function
def prompt():
    level = set_level()
    
    
    role = set_role(level)
    shot = set_shot(level)
    text = set_text()
    main = f'{role} {shot} "{text}"' # role + shot + text
    return main

##############################################
# Nơi cấu trúc AI
completion = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = prompt(),
    max_tokens = 1000, 
    temperature = 0.7

)


response = completion.choices[0].text

# Dữ liệu được trả về
# {
#   "id": "cmpl-1a2b3c4d5e6f7g",
#   "object": "text_completion",
#   "created": 1631486957,
#   "model": "text-davinci-002",
#   "choices": [
#     {
#       "text": "text response from chatGPT",
#       "index": 0,
#       "score": 0.9999999403953552
#     }
#   ]
# }

print(response)

os.system("pause")




