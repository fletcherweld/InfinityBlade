# INFINITY BLADE

Simple, basic, and buggy text adventure game-but I made it!

Infinity Blade runs in the command-line interface (CLI) and can seem scary to approach if you are unfamiliar with the CLI. Don't be alarmed, it should be very easy to follow these instructions. If you get lost, start from the beginning and make sure you have completed every step. If you are still having trouble then look it up!

If you have some of the requirements but not others, follow the directions but simply skip any step you already have done.

## Prerequisites

If you have all four installed, skip ahead to the Infinity Blade specific [Installation](#installation).

- Xcode Command Line Tools

- [Homebrew](https://brew.sh) will help install what you need to run this game (and any other cool projects from GitHub!). This might seem complicated but it is a **much** easier way to install programs.

- [Git](https://git-scm.com/download/mac) which helps transfer the code from GitHub to your local computer (basically).

- Infinity Blade is written in—and runs on—[Python3](https://www.python.org/downloads/).



## Prerequisites Installation Process

This is the installation process for Infinity Blade. Most of this you will only need to do once.

Open the Terminal application. This can be found in Finder in your Applications folder and then your Utilities folder, or simply in Spotlight by pressing command+space and typing Terminal.

### Xcode Command Line Tools

First you need to install the Xcode Command Line Tools if you have never done so. You only need to do this once on your computer.
Copy and paste the following line into your terminal and hit return:
```
sudo xcode-select --install
```
Download the Xcode Command Line Tools (not the whole app) when prompted. First step done!

### Homebrew

Homebrew is a similar installation. You can click the link above if you are curious, but the install is just one line of code. Just as before copy this code, paste it into the terminal, and press return:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
This time there will be no additional popups, but you may have to hit return as the program tells you what it is doing. This may take a moment, but this is also a one time install.

### Git

Git and Python are the easiest to install. Once Homebrew is installed simply copy and paste the next line, and hit return:
```
brew install git
```
As before, this is a one time install and you will not be required to do this again.

### Python

Python should also be installed using Homebrew. (You may be tempted to install Python the "traditional way" through the website, but I promise this is much simpler and also easier to uninstall later if you wish!) Copy and paste the following line into your terminal and hit return:
```
brew install python
```

## Installation


Clone project with git
```
git clone https://github.com/fletcherweld/InfinityBlade.git
```

## Playing



navigate to infinity blade folder

To run the game "python3 infinityblade.py user_name world_name"

You will first need to choose a name for your character and the game world. These are "user_name" and "world_name" respectively. The world of the game will be "world_name" Island.

At the prompt, type python3 infinityblade.py and then two user generated terms needed to run the game.
script, user_name, world_name

```python
print(hello world)
```