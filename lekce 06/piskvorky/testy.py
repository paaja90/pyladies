import pytest
import piskvorky
import util
import ai

def test_vyhodnot():
    assert piskvorky.vyhodnot('abcdef')  

def test_tah():
    assert util.tah('xxxxxx',1,'o')

def test_tah_hrace():
    assert piskvorky.tah_hrace('xxxxxxx')

def test_tah_na_prazdne_pole():
    herni_pole = '--------------------'
    assert len(herni_pole) == 20
    assert herni_pole.count('x') == 1
    assert herni_pole.count('-') == 19
