from yafolder import YaFolder

token = 'AQAAAAA0PDXqAADLW36-u89GxUNZtpYmrRp_Zbk'

if __name__ == '__main__':
    ya = YaFolder(token)
    ya.get_files_list()
    ya.upload_folder('folder76y')