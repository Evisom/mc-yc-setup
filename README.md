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
2. On your low-performance server (or your pc) download [Yandex Cloud CLI](https://yandex.cloud/en/docs/cli/quickstart)

   - run `yc init`
   - enter yout OAuth token
   - configure your profile (just select all default values)
   - as a result - you should get a token after running `yc iam create-token`

3. Also on low-performance server, clone bot folder from this repo.
   - you need to create passwordless ssh connnection between your servers, run `ssh-keygen` on your low-performance server and on your high-performance server add `~/.ssh/id_rsa.pub` (from low-performance server) to `~/.ssh/authorized_keys`, test your connection using `ssh username@host`
   - enter telegramToken,
