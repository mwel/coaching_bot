import ftplib
import constants.FTP_constant

#connect to FTP Server
def connectFTP(ftpHost, ftpUser, ftpPW):
        with ftplib.FTP(constants.FTP_constant.FTP_HOST, constants.FTP_constant.FTP_USER, constants.FTP_constant.FTP_PW ) as ftp:
                print('OK - FTP Connection established.')

# Check for files on FTP Server
def connectFTP(ftpHost, ftpUser, ftpPW):
        with ftplib.FTP(constants.FTP_constant.FTP_HOST, constants.FTP_constant.FTP_USER, constants.FTP_constant.FTP_PW ) as ftp:
                print(ftp.dir())






