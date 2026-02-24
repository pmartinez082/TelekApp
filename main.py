from threading import Thread
from controller.api import run_api
from controller.bot import run_bot

if __name__ == '__main__':
    # Hilo extra para la API
    api_thread = Thread(target=run_api)
    api_thread.daemon = True
    api_thread.start()

    # El bot se lleva el hilo principal
    run_bot()
