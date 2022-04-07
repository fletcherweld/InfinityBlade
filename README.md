# INFINITY BLADE

Simple, basic, and buggy text adventure game-but I made it!

Infinity Blade runs in the command-line interface (CLI) and soley accepts keyboard input to play. This might seem scary to approach if you are unfamiliar with the CLI but don't be alarmed—it should be very easy to follow these instructions. If you get lost, just start from the beginning and double check every step.

If you have some (but not all) of the prereqs listed below, follow the directions but simply skip any step you have already done.

## Prerequisites

If you have all four installed, skip ahead to the Infinity Blade specific [Installation](#installation).

- Xcode Command Line Tools

- [Homebrew](https://brew.sh) will help install what you need to run this game (and any other cool projects from GitHub!). This might seem complicated but it is a **much** easier way to install programs.

- [Git](https://git-scm.com/download/mac) transfers the code from GitHub to your local computer.

- Infinity Blade is written in—and runs on—[Python3](https://www.python.org/downloads/).



## Prerequisites Installation Process

This is the installation process for Infinity Blade. Most of this you will only need to do once.

Open the Terminal application. This can be found in Finder in your Applications folder and then your Utilities folder, or simply in Spotlight by pressing command+space and typing Terminal.

### Xcode Command Line Tools

First you need to install the Xcode Command Line Tools if you have never done so. You only need to do this once on your computer.
Copy and paste the following line into your terminal and hit return:
```
xcode-select --install
```
Download the Xcode Command Line Tools (not the whole app) when prompted. If it asks for a password it is the password you use for your computer. First step done!

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

Python should also be installed using Homebrew (if you haven't already installed it). You may be tempted to install Python the "traditional way" through the website, but I promise this is much simpler and also easier to uninstall later if you wish! Copy and paste the following line into your terminal and hit return:
```
brew install python
```

## Installation

Now you are ready to copy Infinity Blade from GitHub to your computer. You can install wherever you want, but the desktop is an easy option. First you have to change the current directory (this is like clicking the desktop in Finder) to where you want the game. Use this command:
```
cd ~/desktop
```
It is finally time to install Infinity Blade with git. You will copy the project to your desktop with the following command:
```
git clone https://github.com/fletcherweld/InfinityBlade.git
```
Although you will run the game in Terminal, you should see a Folder named InfinityBlade on your desktop. Now that you have the game on your computer, it is time to learn how to run and play it!

## Playing

You will once again change directory to the InfinityBlade folder. If you copied it to your desktop that command would be:
```
cd ~/desktop/InfinityBlade
```
Now it is time to play the game.

To run the game you will type one final command into your terminal and hit return. *Don't just copy and paste this one though!* This is the first opportunity for input from you, the player. You will name your in-game character as well as the in-game world.

The command will be in the following form:
```
python3 infinityblade.py user_name world_name
```
Simply replace user_name with your character's name and world_name with your world name. If you would like to use a name with a space then put quotation marks around that term. For example:
```
python3 infinityblade.py "firstname lastname" randomworld
```
Double check your spelling and then hit return. You are now playing Infinity Blade!

```python
print(hello world)
```

test of `print(inline code)` in `github`.