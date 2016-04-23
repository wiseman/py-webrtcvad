import _webrtcvad


class Vad(object):
    def __init__(self, mode=None):
        self._vad = _webrtcvad.create()
        _webrtcvad.init(self._vad)
        if mode is not None:
            self.set_mode(mode)

    def set_mode(self, mode):
        _webrtcvad.set_mode(self._vad, mode)

    def is_voiced(self, buf, sample_rate, length=None):
        length = length or int(len(buf) / 2)
        if length * 2 > len(buf):
            raise IndexError(
                'buffer has %s frames, but length argument was %s' % (
                    int(len(buf) / 2.0), length))
        return _webrtcvad.process(self._vad, sample_rate, buf, length)


def valid_rate_and_frame_length(rate, frame_length):
    return _webrtcvad.valid_rate_and_frame_length(rate, frame_length)
