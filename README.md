# computer_usage_statistics

Keeps track of what hours of the day the computer is running and logged in on the user. It requires on Python  and unix/linux. Tested on Ubuntu 15.10 and Linux Mint 17 with python 2.7.

In the current setup (which is easy to modify), Cronjob runs a script 4 times per hour which increments the count for that hour in a histogram.
An accompanying function prints an easily readable version of the histogram to the terminal.

# Setting things up
Type in the terminal `chmod +x bash_script` to give the shell permission to run the script. This is neccesary for the cronjob to work.

To schedule a cronjob, type `crontab -e` in the terminal. Be careful not to type `crontab -r`, which will remove all crontab settings.

To the bottom, add `*/15 * * * * /path_to_repository/bash_script`, press ctrl + O to save, accept with enter and ctrl + x to exit. The terminal should output "crontab: installing new crontab" if everything went OK.

Make sure the paths are correctly setup for your computer. Replace all occurrences of /home/ben/Documents/ with whatever path you have to the repository folder. Try `grep /home/ben/ *` from the repository folder to find all such occurences.

# TODO 1
Make an installation file which sets the correct paths. Run it from the repository root folder and it could use pwd and then find all occurences of, say, "REPLACE_THIS_PATH" with the directory obtained from pwd.

# TODO 2
Make the installation file initialize an empty histogram.

A good guide to cronjobs is found at http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/

