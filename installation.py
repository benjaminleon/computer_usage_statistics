# installation.py
# Replaces all occurences of "PATH_TO_REPOSITORY/" with the path to the current working folder.

import os
cwd = os.getcwd()

for filename in ["bash_script", "python_script.py", "print_to_terminal.py"]:
    print filename

    with open(filename, 'r') as myfile:
        text = myfile.read()

    print text
    new_text = text.replace("PATH_TO_REPOSITORY", cwd)
    print new_text

    with open(filename, 'w') as myfile:
        myfile.write(new_text)

# Todo: initialize an empty histogram
