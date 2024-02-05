#!/usr/bin/env python3

# Import libraries that will be used in this script
import re
import os

def main():

    # This is a dictionary:
    chassis_dict = {
              "C": "Compute optimized hyper-scale server",
              "F": "Rack-based sleds for FX2/FX2s enclosure",
              "M": "Modular Blade server",
             "MX": "Modular Blade server",
              "R": "Rack-mountable",
             "XE": "Extreme performance and storage",
             "XR": "Extreme ruggedness"
            }

    # This is a list:
    socket_list = [
             "NA",
             "1 Socket",
             "1 Socket",
             "1 Socket",
             "2 Sockets",
             "2 Sockets",
             "2 Sockets",
             "2 Sockets",
             "2 or 4 sockets",
             "4 Sockets"
            ]

    # This is a list
    gen_list = [
             "Gen 10",
             "Gen 11",
             "Gen 12",
             "Gen 13",
             "Gen 14",
             "Gen 15",
             "Gen 16",
             "Gen 17",
             "Gen 18",
             "Gen 19"
            ]

    # This is a dictionary
    proc_dict = {
            "0": "Intel",
            "5": "AMD"
            }

    os.system('clear')
    code = input("Enter a server code: ")

    # PARSING THE USER INPUT START #################################################
    # This REGEX code snippet is *very* common for parsing input. Use it often!
    # This pattern is looking for letters only, followed by three digits
    # c1 will capture letters, and; c2, c3, and c4 will each collect a single digit
    # code = "R450" would be an example of a MATCH
    # code = "wxq3" would NOT match
    # Could we write a better pattern, YOU BET! Go for it.
    pattern = re.compile(r"""
                             (?P<c1>[a-zA-Z][a-zA-Z]?)
                             (?P<c2>\d)
                             (?P<c3>\d)
                             (?P<c4>\d)
                          """, re.VERBOSE)
    match = pattern.match(code)
    if match:
        # If we get this far, the input matched the REGEX
        code1 = match.group("c1").upper()
        code2 = int(match.group("c2"))
        code3 = int(match.group("c3"))
        code4 = match.group("c4")
    # PARSING THE USER INPUT END #####################################################
    else:
       # If this runs, the user entered an invalid code, so output help info.
       # FIRST ERROR HANDLING OUTPUT STARTS HERE
       print(f"The first character is the chassis type")
       print(f"---------------------------------------------")
       # Use the ".keys" method to lookup the key of each dictionary item
       for key in chassis_dict:
           print (f"{key} = {chassis_dict[key]}")

       print(f"\nThe second character is the socket count")
       print(f"---------------------------------------------")
       # Use the idex value (0-9) to reference each item in a list
       i=0
       for item in socket_list:
           print (f"{i} = {item}")
           i +=1

       print(f"\nThe third character is the generation")
       print(f"---------------------------------------------")
       # Use the idex value (0-9) to reference each item in a list
       i=0
       for item in gen_list:
           print (f"{i} = {item}")
           i +=1

       print(f"\nThe fourth character is the CPU type")
       print(f"---------------------------------------------")
       # Use the ".keys" method to lookup the key of each dictionary item
       for key in proc_dict:
           print (f"{key} = {proc_dict[key]}")
       print(f"---------------------------------------------\n")
       print(f" You entered \"{code}\" which is NOT a dell server code\n")
       print(" You must enter a valid code like r450 or mx345\n")
       print(" Reference the above and PLEASE TRY AGAIN\n")
       # NOTE THE NEXT LINE = EXIT!       
       exit() # No use continuing. Exit the script.
       # FIRST ERROR HANDLING ENDS HERE

    # If we got this far, all four codes passed the regex test,
    # but additional validity testing is necessary
    print(f"Looking up Dell {code1}{code2}{code3}{code4}:")

    if code1 in chassis_dict:
        # If code1 can be found in the code1 dictionary, it is valid, so print it.
        print(f"  {code1} = {chassis_dict[code1]}")
    else:
        # Else the code was not found so start error handling
        # code1 ERROR HANDLING STARTS
        print(f" {code1} is invalid, valid codes are:")
        for key in chassis_dict:
            print (f"    {key} = {chassis_dict[key]}")
        #code1 ERROR HANDLING ENDS

    if 1 <= code2 <= 9:
        # If code2 is a single digit 1-9, it is valid, print it
        print(f"  {code2} = {socket_list[code2]}")
    else:
        # Else it is not valid, so handle the error
        #code2 ERROR HANDLING STARTS
        print(f"  {code2} is invalid. Valid CPU socket codes are:")
        i=0
        for item in socket_list:
            print (f"    {i} = {item}")
            i +=1
        #code2 ERROR HANDLING ENDS    

    if 0 <= code3 <= 9:
       # If code3 is a single digit 0-9, it is valid, print it
       print(f"  {code3} = {gen_list[code3]}")
    else:
        # Hmmm, this should NEVER happen, but let's write a defensive
        # error handler in spite of that.
        #code3 ERROR HANDLING STARTS
        print(f" error: {code3} Must be 0 to 9")
        i=0
        for item in gen_list:
            print (f" {i} = {item}")
            i +=1
        #code3 ERROR HANDLING ENDS

    if code4 in proc_dict:
        # If code4 is found, print it
        # Wow, error handling with dictionaries seems easier!
        print(f"  {code4} = {proc_dict[code4]}")
    else:
        # else the code was not found, so handle the error
        #code4 ERROR HANDLING STARTS
        print(f"  {code4} is invalid, here are valid options:")
        for key in proc_dict:
           print (f"     {key} = {proc_dict[key]}")
        #code4 ERROR HANDLING ENDS

if __name__ == "__main__":
    main()           

