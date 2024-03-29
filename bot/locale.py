from config import config

LOCALE = {
    "LANGUAGES": {
        "ENGLISH" : 0,
        "RUSSIAN" : 1
    },
    "ACCESS_DENIED": (
        "you can't control the server from this chat, if you are an admin, add ID to allowed_chats and reboot the bot. ID: ",
        "ты не можешь управлять сервером из этого чата, если ты админ, то добавь ID в allowed_chats и перезагрузи бота. ID: "
    ),
    "SERVER_STARTED": (
        "server started successfully, wait a couple of minutes and you're ready to play!\nMinecraft URL: " + config['minecraft_host'],
        "сервер успешно запущен, подожди пару минут и можно будет играть!\nMinecraft URL: " + config['minecraft_host']
    ),
    "SERVER_STOPPED": (
        "server stopped successfully!",
        "сервер успешно выключен!"
    ),
    "SERVER_ALREADY_RUNNING" : (
        "server already running!",
        "сервер уже был запущен!"
    ), 
    "SERVER_ALREADY_STOPPED": (
        "server already stopped!",
        "сервер уже был выключен!"
    ),
    "SERVER_ERROR": (
        "server error😾",
        "ошибка на сервере😾"
    ),
    "BACKUP_IN_PROGRESS": (
        "backup in progress...",
        "резервная копия создается..."
    ), 
    "BACKUP_SUCCESS": (
        "backup created successfully!\nBackup URL: " + config['backup_host'],
        "резервная копия успешно создана!\nMinecraft URL: " + config['backup_host']
    ),
    "UNABLE_TO_BACKUP": (
        "server is down, unable to create a backup",
        "сервер выключен, нельзя сделать резервную копию"
    ),
    "HELP": (
        "/start - starts a server\n/stop - shuts down the server\n/status - prints list of players online\n/backup - create a backup of the world\n/backup_and_stop - create a backup and shuts down the server\n",
        "/start - включает сервер\n/stop - выключает сервер\n/status - показывает игроков онлайн\n/backup - создает резервную копию\n/backup_and_stop - создает резервную копию и выключает сервер\n"
    )
}