# SETUP

## Required Software

- [Python](https://www.python.org/downloads/) >= 3.10
- [Git](https://git-scm.com/)

### Nice to have
- [Visual Studio Code](https://code.visualstudio.com/?wt.mc_id=vscom_downloads)
    - VS Code Extensions:
        - [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
        - [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
        - [GitLens](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Getting Started

Firstly, please install the software detailed above :)
### Git

Git is a [version control](https://about.gitlab.com/topics/version-control/) system intended for use with software development. Software like git is essential for keeping tack of every change to a codebase ensuring that we know exactly when all changes were made, and have the freedom to roll back to an earlier version if required. (i.e. Essential to have in events such as our groundbreaking feature actually bricks the software rendering it useless...)

New to Git? Visit (https://docs.github.com/en/get-started/getting-started-with-git) for more information!

After you have installed Git, open up a terminal (**terminal** on MacOS, **CMD**, or **Windows Terminal** on Windows)*.

After you have installed Git (and preferably VS Code), please navigate to the desired folder/directory you would like this code to be in (i.e. Documents). Almost all Operating Systems will support `cd [folder-path]` (change-directory), check out [this cheatsheet](https://terminalcheatsheet.com/) for more details.

Once you are in the directory you'd like (i.e. Documents/Neurotech/) run the following command:

    git clone https://github.com/LeonardoFerrisi/neurotech-boilerplate.git

*If you are on any form of linux, I'm going to go and assume you know all of this info already so will not bore you with the basic details of setting up this environment

### Python and Python Virtual Environments

This collection of boilerplates is mostly written in python for ease of use to new and experienced programmers. 

This project relies on several python *packages* which are detailed in [requirments.txt](). You can either install these to your global python environment or a local python environment. It is typically easier for future development if you rely on the local python environment. 

#### Python Virtual Environment

After you have installed Python on your machine do the following:

Open a Terminal as you did in the Git setup, navigate to the desired folder, and run the following command: 

    python -m venv .neurotech-env

This will setup a python virtual environment in the directory you are currently in. Activate the virtual environment using the following:

*NOTE: Including a '`.`' in front of your environment name allows it to be auto-detected by VS Code when working with Python. Not essential but convientient.*
##### If on Windows

    .neurotech-env/Scripts/activate

##### If on MacOS/Linux

    source .neurotech-env/bin/activate

You should then see an indicator that you are in the environment such as 

`(.neurotech-env) C:\path\to\neurotech-boilerplate>` (on windows machine)

You now are good to run the following command to install all required packages:

    python -m pip install -r requirments.txt



