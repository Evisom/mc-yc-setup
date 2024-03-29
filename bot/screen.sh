screen -AdmS mc-yc-bot  bash -c 'until python3 main.py; do echo crashed; sleep 1; done'
