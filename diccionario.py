
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "MEME": "Una imagen o video chistoso",
            "FRANCIA": "Un pais inventado que no existe"
            }

palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if palabra in meme_dict.keys():
    print (meme_dict[palabra])
else:
    print ("no esta")
