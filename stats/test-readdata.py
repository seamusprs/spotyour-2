import spotyour-2.readdata
import unittest

class TestPlaylist(unittest.TestCase):
    """Test the playlist functions in the readdata module, based on the default playlist included in the spotyour package"""

    def test_getplaylist(self):
        testpl = readdata.Playlist("playlist")
        self.assertTrue(type[testpl] is readdata.Playlist)

    def test_lengthproperty(self):
        testpl = readdata.Playlist("playlist")
        self.assertEqual(testpl.length, 708)
        

class TestSong(unittest.TestCase):
    """Test the song functions in the readdata module, based on a specific song in the default playlist """

    def test_getsong_id(self):
        testpl = readdata.Playlist("playlist")
        testsong = readdata.Song(testpl, "3QZ7uX97s82HFYSmQUAN1D")
        self.assertTrue(type[testsong] is readdata.Song)

    def test_getsong_index(self):
        testpl = readdata.Playlist("playlist")
        testsong = readdata.Song(testpl, 15)
        self.assertTrue(type[testsong] is readdata.Song)

    def test_getsongs(self):
        testpl = readdata.Playlist("playlist")
        testsong1 = readdata.Song(testpl, "3QZ7uX97s82HFYSmQUAN1D")
        testsong2 = readdata.Song(testpl, 15)
        self.assertEqual(testsong1, testsong2)

    def test_artistproperty(self):
        testpl = readdata.Playlist("playlist")
        testsong = readdata.Song(testpl, "3QZ7uX97s82HFYSmQUAN1D")
        self.assertEqual(testsong.artist, "Pink Floyd")

    