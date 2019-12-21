import logging

 
def main():
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format='%(levelname)s: %(message)s' )
    logging.info('Starting') 
    logging.error('Error')  


if __name__ == '__main__':
    main()
