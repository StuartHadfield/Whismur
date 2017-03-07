import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../lib/")
from utils import audio_reader as ar


def test_read():
    [sample_rate, data] = ar.read_audio_file("samples/around_the_world-atc.wav")
    print "it should read a sample rate"
    assert sample_rate == 22050
    print "it should read wav data"
    assert data.size == 4814784


def test_failed_read():
    with pytest.raises(IOError) as excinfo:
        ar.read_audio_file("imaginary_file.wav")

    assert "The file could not be found" in str(excinfo.value)
