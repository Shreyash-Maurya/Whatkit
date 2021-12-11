# importing the module
import pywhatkit
 
# using Exception Handling to avoid
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+919423115128",
                        "Test Message From shreyash ",
                        22, 28)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")