# mc-yc-bot

> Setup for low-budget Minecraft players who cannot afford to keep a high-performance server on always

Structure:

- Minecraft server (high-performance Yandex Cloud server)
- Telegram bot (low-performance machine or your pc)

How it works?

1.  You create a group chat with your friends
2.  When players want to play, they turn on server using `/start` in chat
3.  ✨Server works✨
4.  When you are tired of playing, use `/stop` to turn off the server

Telegram commands:

- `/start` - Start a machine on Yandex Cloud
- `/stop` - Shuts down the server
- `/status` - Prints list of players online
- `/backup` - Create a backup of the world
- `/backup_and_stop` - Create a backup and shuts down the server

How to configure

0. Create telegram bot using `@BotFather` and create chat with your friends
1. Create an instance on Yandex Cloud (2 CPU's + 4gbs of RAM is optimal imo)
2. High-performance server
   - Install Docker
   - Clone server folder from this repo
   - Add your low-performance ssh key to `~/.ssh/authorized_keys`
   - Build Docker image using `build.sh`
   - Run Docker container using `run.sh`
   - NOTE: you can copy your world into `server/world`
3. Low-performance server (or your pc)
   - Download [Yandex Cloud CLI](https://yandex.cloud/en/docs/cli/quickstart)
   - Configure yc-cli, run `yc init`, enter your OAuth token
   - As a result - you should get a token after running `yc iam create-token`
   - Clone `bot` folder
   - Install dependencies using `pip3 install`
   - Enter all required fields in config.py,
   - Install screen (`sudo apt-get install screen` for Debain based distros)
   - run `screen.sh`
