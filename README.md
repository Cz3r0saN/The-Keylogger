# The-Keylogger
The simple and straight keylogger 
Hello everyone Its Zer0 here today I am implementing an simple keylogger program with the help of python language this is just a sample project I made a long time ago . Here's a short description about the file 
( Note : the provided files are only for educational purposes I do not intend or support and promote any unwanted or unethical behaviour , Please be careful while using the provided script . And again happy hacking !!! )
The libraries I used were :

------------------------------------------------------------------------
1. pynput
Purpose: The pynput library allows you to control and monitor input devices such as keyboards and mice. It provides a simple interface to listen for events and simulate input.
------------------------------------------------------------------------

Along with the libraries there were "Key components"  which included : 

a. keyboard
Module: The keyboard module within pynput is specifically designed for keyboard events.
Listener: The Listener class is used to monitor keyboard events. It runs in a separate thread, allowing it to capture keystrokes without blocking the main program.

b. on_press function
Event Handler: This function is called whenever a key is pressed. It takes a single argument, key, which represents the key that was pressed.

---------> Key Handling <---------
Normal Keys: If the key is a standard character (like letters and numbers), it attempts to write key.char to the log file.
Special Keys: If the key is a special key (like Shift, Ctrl, or Enter), it raises an AttributeError when trying to access key.char. In this case, the code writes the string representation of the key (e.g., [Key.enter]) to the log file.

c. with keyboard.Listener(on_press=on_press) as listener
Listener Context Manager: This line creates an instance of the Listener class, specifying on_press as the callback function to handle key press events. The listener will run until it is stopped (e.g., by pressing Ctrl+C).
listener.join(): This method blocks the program from exiting and keeps the listener active, allowing it to capture keystrokes.


----------------------------------------------------------------------------
