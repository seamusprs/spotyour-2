import spotyour2.stats.readdata as rd
import unittest

class TestPlaylist(unittest.TestCase):
    """Test the playlist functions in the readdata module, based on the default playlist included in the spotyour package"""

    @classmethod
    def setUpClass(TestPlaylist):
        TestPlaylist.testpl = rd.Playlist("spotyour2/playlist")

    def setUp(self):
        self.testpl = rd.Playlist("spotyour2/playlist")

    def tearDown(self):
        self.testpl = None

    @classmethod
    def tearDownClass(TestPlaylist):
        TestPlaylist.testpl = None

    def test_getplaylist(self):
        self.assertTrue(type(self.testpl) is rd.Playlist)

    def test_lengthproperty(self):
        self.assertEqual(self.testpl.length, 708)
        

class TestSong(unittest.TestCase):
    """Test the song functions in the readdata module, based on a specific song in the default playlist """

    @classmethod
    def setUpClass(TestSong):
        testpl = rd.Playlist("spotyour2/playlist")
        TestSong.testsong = rd.Song(testpl)

    def setUp(self):
        self.testpl = rd.Playlist("spotyour2/playlist")
        self.testsong = rd.Song(self.testpl, "3QZ7uX97s82HFYSmQUAN1D")

    def tearDown(self):
        self.testpl = None
        self.testsong = None

    @classmethod
    def tearDownClass(TestPlaylist):
        TestSong.testsong = None

    def test_getsong_id(self):
        msong = rd.Song(self.testpl, "3QZ7uX97s82HFYSmQUAN1D")
        self.assertTrue(msong.id == "3QZ7uX97s82HFYSmQUAN1D")

    def test_getsong_index(self):
        msong = rd.Song(self.testpl, 15)
        self.assertTrue(msong.id == "3QZ7uX97s82HFYSmQUAN1D")

    def test_getsongs(self):
        msong = rd.Song(self.testpl, "3QZ7uX97s82HFYSmQUAN1D")
        self.assertEqual(msong.id, self.testsong.id)

    def test_properties(self):
        self.assertEqual(self.testsong.id, "3QZ7uX97s82HFYSmQUAN1D")
        self.assertEqual(self.testsong.track, "Tom Sawyer")
        self.assertEqual(self.testsong.album, "Moving Pictures (2011 Remaster)")
        self.assertEqual(self.testsong.release, "1981-02-12")
        self.assertEqual(self.testsong.duration, 276880)
        self.assertEqual(self.testsong.genre, "album rock,canadian metal,classic canadian rock,classic rock,hard rock,progressive rock,rock")
        self.assertEqual(self.testsong.label, "Mercury Records")
        self.assertEqual(self.testsong.tempo, 87.559)

    