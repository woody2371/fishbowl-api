from ftplib import FTP
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')

ftp = FTP()
ftp.connect(cfg['FTP']['host'],int(cfg['FTP']['port']))
ftp.login(user=cfg['FTP']['user'], passwd = cfg['FTP']['passwd'])

def grabFile(filename):

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()

def placeFile(filename):

    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()
