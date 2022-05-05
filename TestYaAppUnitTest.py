from yafolder import YaFolder
import unittest

token = 'AQAAAAA0PDXqAADLW36-u89GxUNZtpYmrRp_Zbk'


class TestYaAppUnitTest(unittest.TestCase):

    def test_ya_folder(self):
        ya = YaFolder(token)
        self.assertEqual(201, ya.upload_folder('test'))

    def test_ya_check(self):
        ya = YaFolder(token)
        ya.upload_folder('folder15')
        json = ya.get_files_list()
        json_data = json['_embedded']['items']
        lst = []
        for d in json_data:
            for key in d.items():
                for item in key:
                    lst.append(item)
        self.assertIn('folder15', lst[1])