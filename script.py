# coding: utf_8
import setting
import math

def vowel(phoneme):
    syllabary = {
        "あかさたなはまやらわがざだばぱぁゃ" : "a",
        "いきしちにひみ  り  ぎじぢびぴぃ" : "i",
        "うくすつぬふむゆる  ぐずづぶぷぅゅ" : "u",
        "えけせてねへめ  れ  げぜでべぺぇ" : "e",
        "おこそとのほもよろをごぞどぼぽぉょ" : "o"
    }
    for a in syllabary.keys():
        if phoneme in a:
            return syllabary[a]
    return 'n'


with open(setting.RPPpath, mode='r',errors='replace', encoding='utf-8') as f:
    RPP = f.readlines()
    MediaItemsP = []
    MediaItemsL = []
    MediaItemsLyric = []

    for index in range(len(RPP)):
        if  RPP[index].find("<ITEM") != -1:
            if RPP[index+1].find("POSITION") != -1 and RPP[index+3].find("LENGTH") != -1:
                MediaItemsP.append(
                    float(RPP[index+1].split("POSITION ")[1][:-1]))
                MediaItemsL.append(
                    float(RPP[index+3].split("LENGTH ")[1][:-1]))
            else:
                print("異常:RPPが変")
        if "<x" in RPP[index].lower():
            MediaItemsLyric.append(RPP[index].split(" ")[-1][:-1])

#全体の長さ計算
Length = MediaItemsP[0]+MediaItemsL[0]
MediaItemsL.pop(0)
MediaItemsP.pop(0)

if len(MediaItemsL)!= len(MediaItemsP) or len(MediaItemsL)!= len(MediaItemsLyric) :
    print("メディアアイテム数と歌詞文字数が異なります。正常に動作していない可能性が高いです。")

#口パクAVIのパス設定
LipPath = {
    "n" : setting.LIPPath.replace("*", "n"),
    "a" : setting.LIPPath.replace("*", "a"),
    "i" : setting.LIPPath.replace("*", "i"),
    "u" : setting.LIPPath.replace("*", "u"),
    "e" : setting.LIPPath.replace("*", "e"),
    "o" : setting.LIPPath.replace("*", "o")
}

Exotext = ""

with open(setting.TEMPLATEPath, mode='r',errors='replace', encoding='shift_jis') as f:
    TEMPLATE = f.read()
    exoheader, exoloop = TEMPLATE.split("{{LOOP}}\n")
    exoheader = exoheader.replace("{{END}}", str(math.ceil(Length)*60))
    exoheader = exoheader.replace("{{RATE}}", str(setting.FPS))
    exoheader = exoheader.replace("{{FILE_N}}", LipPath["n"])
    Exotext += exoheader
    for index in range(len(MediaItemsP)):
        MediaItemsPFrame = round(MediaItemsP[index] * setting.FPS)+1
        MediaItemsEFrame = round(MediaItemsP[index] * setting.FPS )+round( MediaItemsL[index] * setting.FPS)
        exolooptmp = exoloop.replace("{{ITEM_COUNT}}", str(index+1))
        exolooptmp = exolooptmp.replace("{{LOOP_START}}", str(MediaItemsPFrame))
        exolooptmp = exolooptmp.replace("{{LOOP_END}}", str(MediaItemsEFrame))        
        exolooptmp = exolooptmp.replace("{{LAYER}}", str(index%2+2))
        exolooptmp = exolooptmp.replace("{{FILE}}", LipPath[vowel(MediaItemsLyric[index])])
        Exotext += "\n"+exolooptmp

with open(setting.ExportPath, mode='w',errors='replace', encoding='shift_jis') as f:
    f.write(Exotext)