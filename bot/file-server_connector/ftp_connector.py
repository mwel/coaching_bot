import ftplib
import constants.FTP_constant

with ftplib.FTP_TLS(constants.FTP_constant.FTP_HOST, constants.FTP_constant.FTP_USER, constants.FTP_constant.FTP_PW ) as ftp:
