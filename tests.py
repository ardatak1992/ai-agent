import unittest
from functions.get_files_info import get_files_info

class TestMain(unittest.TestCase):
  def test_1(self):
    files = get_files_info("calculator", ".")
    print(files)
    self.assertEqual(files, """Result for current directory:
                                - main.py: file_size=576 bytes, is_dir=False
                                - tests.py: file_size=1343 bytes, is_dir=False
                                - pkg: file_size=92 bytes, is_dir=True
                     """)
  
  def test_2(self):
    files = get_files_info("calculator", "pkg")
    self.assertEqual(files, """Result for current directory:
                                - main.py: file_size=576 bytes, is_dir=False
                                - tests.py: file_size=1343 bytes, is_dir=False
                                - pkg: file_size=92 bytes, is_dir=True
                     """)

  def test_3(self):
    files = get_files_info("calculator", "/bin")
    print(files)

  def test_4(self):
    files = get_files_info("calculator", "../")
    print(files)


if __name__ == "__main__":
    unittest.main()
