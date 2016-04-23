.. image:: https://travis-ci.org/wiseman/py-webrtc-vad.svg?branch=master
    :target: https://travis-ci.org/wiseman/py-webrtc-vad

py-webrtcvad
============

This is a python interface to the WebRTC Voice Activity Detector
(VAD).  It is compatible with Python 2 and Python 3.

A `VAD <https://en.wikipedia.org/wiki/Voice_activity_detection>`
classifies a piece of audio data as being voiced or unvoiced. It can
be useful for telephony and speech recognition.

The VAD that Google developed for the `WebRTC <https://webrtc.org/>`
project is reportedly one of the best available, being fast, modern
and free.

How to use it
-------------

1. Create a `Vad` object.

  import webrtcvad
  vad = webrtcvad.Vad()

2. Optionally, set its aggressiveness mode, which is an integer
   between 0 and 3. 0 is the least aggressive about filtering out
   non-speech, 3 is the most aggressive.

  vad.set_mode(1)

3. Give it a short segment ("frame") of audio. The WebRTC VAD only
   accepts 16-bit mono PCM audio, sampled at 8000, 16000, or 32000 Hz.
   A frame must be either 10, 20, or 30 ms in duration.

  sample_rate = 16000
  frame_duration = 10  # ms
  frame = b'\x00\x00' * sample_rate * frame_duration / 1000
  print 'Contains speech: %s' % (vad.is_voiced(frame, sample_rate)

API
---

class webrtc.Vad(*mode=None*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VAD constructor.

*mode* is the aggressiveness mode.  Should be between 0 and 3.

**set_mode**(*mode*)

Sets the aggressiveness mode of a VAD.

.. function:: spam(eggs)
              ham(eggs)
   :noindex:

   Spam or ham the foo.
