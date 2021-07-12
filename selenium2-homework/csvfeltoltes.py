import os

if os.name == 'nt':
    import ctypes
    from ctypes import windll, wintypes
    from uuid import UUID


    # ctypes GUID copied from MSDN sample code
    class GUID(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", wintypes.BYTE * 8)
        ]

        def __init__(self, uuidstr):
            uuid = UUID(uuidstr)
            ctypes.Structure.__init__(self)
            self.Data1, self.Data2, self.Data3, \
            self.Data4[0], self.Data4[1], rest = uuid.fields
            for i in range(2, 8):
                self.Data4[i] = rest >> (8 - i - 1) * 8 & 0xff


    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(GUID), wintypes.DWORD,
        wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
    ]


    def _get_known_folder_path(uuidstr):
        pathptr = ctypes.c_wchar_p()
        guid = GUID(uuidstr)
        if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
            raise ctypes.WinError()
        return pathptr.value


    FOLDERID_Download = '{374DE290-123F-4565-9164-39C4925E467B}'


    def get_download_folder():
        return _get_known_folder_path(FOLDERID_Download)
else:
    def get_download_folder():
        home = os.path.expanduser("~")
        return os.path.join(home, "Downloads")
import csv
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/another_form.html')


def find_and_fill_element(id, element_value):
    element = driver.find_element_by_id(id)
    element.clear()
    element.send_keys(element_value)


send_button = driver.find_element_by_id('submit')
download_button = driver.find_element_by_xpath('//div/button')

original_rows = []
csvfile = open('csv.csv', 'r', encoding="utf-8")
csvreader = csv.reader(csvfile, delimiter=',')
next(csvreader)
for row in csvreader:
    original_rows.append(row)
    find_and_fill_element('fullname', row[0])
    find_and_fill_element('email', row[1])
    find_and_fill_element('dob', row[2])
    find_and_fill_element('phone', row[3])
    send_button.click()

outputfile_name = os.path.join(get_download_folder(), "table.csv");
if os.path.exists(outputfile_name):
    os.remove(outputfile_name)


def equal_row(row1, row2):
    return row1 == row2


download_button.click()
time.sleep(5)

with open(outputfile_name, 'r', encoding="utf-8") as outputfile:
    outputreader = csv.reader(outputfile, delimiter=',')
    next(outputreader)
    number = 0
    for row in outputreader:
        assert (equal_row(row, original_rows[number]) == True)
        number += 1
    assert (number == len(original_rows))

csvfile.close()
driver.close()
