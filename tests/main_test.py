"""Test module."""
import unittest
import glob
import os
import re
import shutil

from app.main import main
from app.main import download

class TestMain(unittest.TestCase):
    """Main test class."""

    def test_download(self):
        """Test download functionality."""
        args = dict()
        args['arch'] = "amd64"
        md5_hash = download(args)
        self.assertEqual(md5_hash, "d00bf88e20a9167d72c15f914e2f6ae6")

    def test_main(self):
        """Test main functionality."""
        contents_files = glob.glob("./tests/Contents-*")

        for file in contents_files:
            # Copy the mock file in place
            shutil.copyfile(file, f"./{os.path.basename(file)}")
            result = re.search(r"Contents-(.*)$", file)
            arch = result.group(1)
            print(f"Testing arch {arch} ---->")
            args = dict()
            args['arch'] = arch
            stats = main(args)

            file = open(f"./tests/Stats-{arch}")
            correct_stats = file.read()
            file.close()
            # Check that the correct statistics are returned
            self.assertEqual(stats, correct_stats)


if __name__ == "__main__":
    unittest.main()
