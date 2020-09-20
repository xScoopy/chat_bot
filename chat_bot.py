#importing choice for random selection of responses
from random import choice

#Character customization chatbot
print("Welcome to the Facial Feature Creator Bot!")
print("If you're stuck on what your next character should look like, you've come to the perfect spot for inspiration.")
print("Currently I can assist with many facial features including eyes, nose, mouth, ears, and chin")

#Creation of function : get_bot_response()
def get_bot_response(user_response) :

    #Creation of Bot response lists:
    #Nose list
    bot_response_nose = ["Make it long and narrow", "Short and stubby", "Crooked with one nostril", "Two dots for nostrils"]
    #Mouth list
    bot_response_mouth = ["Skinny bird lips!", "Crooked smile", "Throw some botox in there", "Super wide like the Joker"]
    #Ear list
    bot_response_ear = ["Big floppy ears", "Droopy earlobes", "Pointy like an elf!", "Normal ears wouldn't hurt"]
    #Eye list
    bot_response_eye = ["Big blue eyes!", "Go for the Green", "Beautiful brown", "Rambunctious Red!", "All black(like a demon)"]
    #Chin list
    bot_response_chin = ["super cleft chin", "Wide powerful jawline", "Pointy chin!"]
    
    #conditionals for user responses
    if user_response.upper() == "NOSE":
        return choice(bot_response_nose)
    elif user_response.upper() == "MOUTH":
        return choice(bot_response_mouth)
    elif user_response.upper() == "EAR" or "EARS":
        return choice(bot_response_ear)
    elif user_response.upper() == "EYE" or "EYES":
        return choice(bot_response_eye)
    elif user_response.upper() == "CHIN" or "JAW":
        return choice(bot_response_chin)
    else:
        return "That's not a facial feature I'm able to help out with quite yet, please try a different selection or type 'done' to quit. "
    

#Gather user response 
user_response = ""
while True:
    user_response = input("Which facial feature would you like a suggestion for? ")
    if user_response.upper() == "DONE":
        break
    
    bot_response = get_bot_response(user_response)
    print(bot_response)  