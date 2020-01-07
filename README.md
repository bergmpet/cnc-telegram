# C&C Telegram Bot

Simple Python 3 implementation of Command and Control bot. It implements four possible commands:
* List files in a specified directory
* List all active users
* List all running processes
* Write data to a specified file

Some of the commands are implemented by calling the Linux shell commands. On Windows some of them may not be available. The bot checks Telegram for new incoming messages every 15 seconds.

## Example of communication

![Communication](./imgs/comm.gif)

## Installation
### Obtaining the API key
First of all, you need to have a Telegram account. Afterwards, you need to follow the steps given by the [Telegram BotFather](https://telegram.me/botfather). It is a Telegram interface for creation of user's bots. Starting with command `/newbot` you will be asked for the name of your bot and its username. At the end of the process the BotFather will give you your API key.

### Running the bot
 Once you have your API key, you need to paste it to the file `authorization.py`. Once it is done, you can install the requirements `pip install -r requirements.txt` and run the bot using command `python3 bot.py`.

In your Telegram application simply start conversation with your bot. Once it's started the message showing possible commands is shown. Using the chat you can send all of the possible commands, bot will execute them and send you a message with the result of operations.

## Commands

* Directory listing: `ls [path]`  
* Show active users: `users`  
* Show running processes: `processes`  
* Write to file: `write [path] [data]`  
* Terminate the application: `terminate`  
