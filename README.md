[![Version](https://img.shields.io/pypi/StuartHadfield/Whismur.svg)](https://badge.fury.io/py/StuartHadfield/Whismur)  [![Build](https://img.shields.io/travis/StuartHadfield/Whismur.svg)](https://travis-ci.org/StuartHadfield/Whismur)  [![Coverage](https://img.shields.io/codecov/c/github/StuartHadfield/Whismur.svg)](https://codecov.io/github/StuartHadfield/Whismur)  [![Documentation Status](https://readthedocs.org/projects/whismur/badge/?version=latest)](http://whismur.readthedocs.io/en/latest/?badge=latest)

# Readme

## Whismur

<center>![alt tag](http://orig01.deviantart.net/fc9a/f/2015/050/7/5/_293_whismur_by_badangel2012-d8ipi1e.png)</center>
<sub><sup>_Picture from badangel on deviantart!_</sup></sub>

## Description

Whismur is a python based sound wave analysis tool.  It aims to be able to classify unknown soundwaves as either music or speech using choosable ML techniques such as the kNN algorithm.  The idea is a user inputs a soundwave and specifies a technique after having trained the classifier.

I hope to extend this library to perform a variety of audio functions such as cleaning, trimming, silence removal, noise suppression, audio visualization, word recognition etc.

The fundamental idea is for a user to run:

```
python whismur.py --file=audio.wav --classifier=knn --visualize=true --trim_silence=true --bpm=true
```

And Whismur looks at audio.wav file, check is it music or is it speech, what classifier, a visualization of the classification process, trim all the silence from the clip, what is the BPM if it is music etc., this is a very early stage and high level description of course.
