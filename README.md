# computer_usage_statistics

Keeps track of what hours of the day the computer is running and logged in on the user. It requires Python  and unix/linux. Tested on Linux Mint 17 and python 2.7.

In the current setup (which is easy to modify), Cronjob runs a script 4 times per hour which increments the count for that hour in a histogram.
An accompanying function prints an easily readable version of the histogram to the terminal.

# Setting things up

Run the installation script by navigating to the folder containing the files and enter `python installation.py` in your terminal. This will replace all occurences of PATH_TO_REPOSITORY with the actual path to the repository on your computer.

Type in the terminal `chmod +x bash_script` to give the shell permission to run the script. This is neccesary for the cronjob to work.

To schedule a cronjob, type `crontab -e` in the terminal. Be careful not to type `crontab -r`, which will remove all crontab settings.

When adding the cronjob, go to the bottom and add `*/15 * * * * /path_to_repository/bash_script` to run the script every 15 minutes. Press ctrl + o to save, accept with enter and ctrl + x to exit. The terminal should output "crontab: installing new crontab" if everything went OK.

A good guide to cronjobs is found at http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/

# Usage
After everything is set up, the cronjob will take care of running the script at regular intervals (when the user is logged in).

To show the results, run `python /PATH_TO_FOLDER/print_to_terminal.py`.

If a user would like to simply type `show_usage` in the terminal and get the same output, an alias can be made. To create an alias that lasts even after a log out and log in, edit the bashrc file, for example type `nano ~/.bashrc`. At the bottom, add `alias show_usage='python PATH_TO_FOLDER/print_to_terminal.py', with PATH_TO_FOLDER as your actual path to the folder. The alias will not take effect in the current terminal, but open a new one and it will work for that one and all the other terminals you open.




