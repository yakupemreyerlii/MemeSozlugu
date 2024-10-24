meme_dict = {
    "LOL": "Komik bir şeye verilen cevap",
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}

print("Programda bulunan kelimeler:")
for word in meme_dict.keys():
    print(word)

for _ in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(word,"kelimesinin anlamı",meme_dict[word])
    else:
        print("Üzgünüm",word,"sözlükte bulunamadı.")

print("Teşekkürler! Programı kullandığınız için memnun olduk.")