import unittest

import webrtcvad


class WebRtcVadTests(unittest.TestCase):
    def test_constructor(self):
        vad = webrtcvad.Vad()

    def test_set_mode(self):
        vad = webrtcvad.Vad()
        vad.set_mode(0)
        vad.set_mode(1)
        vad.set_mode(2)
        vad.set_mode(3)
        self.assertRaises(
            ValueError,
            vad.set_mode, 4)

    def test_valid_rate_and_frame_length(self):
        self.assertTrue(webrtcvad.valid_rate_and_frame_length(8000, 160))
        self.assertTrue(webrtcvad.valid_rate_and_frame_length(16000, 160))
        self.assertFalse(webrtcvad.valid_rate_and_frame_length(32000, 160))
        self.assertRaises(
            ValueError,
            webrtcvad.valid_rate_and_frame_length, 2 ** 35, 10)

    def test_process_zeroes(self):
        frame_len = 160
        self.assertTrue(
            webrtcvad.valid_rate_and_frame_length(8000, frame_len))
        sample = b'\x00' * frame_len * 2
        vad = webrtcvad.Vad()
        self.assertFalse(vad.is_speech(sample, 16000))

    def test_process_file(self):
        with open('test-audio.raw', 'rb') as f:
            data = f.read()
        frame_ms = 30
        n = int(8000 * 2 * 30 / 1000.0)
        frame_len = int(n / 2)
        self.assertTrue(
            webrtcvad.valid_rate_and_frame_length(8000, frame_len))
        chunks = list(data[pos:pos + n] for pos in range(0, len(data), n))
        if len(chunks[-1]) != n:
            chunks = chunks[:-1]
        expecteds = [
            '011110111111111111111111111100',
            '011110111111111111111111111100',
            '000000111111111111111111110000',
            '000000111111111111111100000000'
        ]
        for mode in (0, 1, 2, 3):
            vad = webrtcvad.Vad(mode)
            result = ''
            for chunk in chunks:
                voiced = vad.is_speech(chunk, 8000)
                result += '1' if voiced else '0'
            self.assertEqual(expecteds[mode], result)
