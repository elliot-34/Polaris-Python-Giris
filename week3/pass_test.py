from passwordsystem import check

def test_dogru():
    assert check("1@A")=="Güçlü Şifre.Kabul Edildi."
    assert check("afsA1fa@aAS3")=="Güçlü Şifre.Kabul Edildi."

def test_buyukharfyok():
    assert check("1@asdasd5!")=="Güçsüz Şifre Tekrar deneyiniz."

def test_ozelkarakteryok():
     assert check("11AsdwA4")=="Güçsüz Şifre Tekrar deneyiniz."

def test_sayiyok():
    assert check("adfwA@afaA.")=="Güçsüz Şifre Tekrar deneyiniz."