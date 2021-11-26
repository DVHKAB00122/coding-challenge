from search_term_data.BackgroundProcess import BackgroundProcess


def main():
    background_process = BackgroundProcess()
    background_process.start_daemon()


if __name__ == '__main__':
    main()
