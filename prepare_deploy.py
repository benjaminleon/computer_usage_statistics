# prepare_deploy.py
# Replaces all occurences of "/home/ben/Documents/" with the template path PATH_TO_REPOSITORY. This is used in the deploy and when installing, PATH_TO_REPOSITORY is replaced by the actual path to the repository folder.

for filename in ["bash_script", "python_script.py", "print_to_terminal.py"]:
    print filename

    with open(filename, 'r') as myfile:
        text = myfile.read()


    print text
    new_text = text.replace("/home/ben/Documents/computer_usage_statistics/", "PATH_TO_REPOSITORY/")
    print new_text
    
    with open(filename, 'w') as myfile:
        myfile.write(new_text)


