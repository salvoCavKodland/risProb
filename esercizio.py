meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }
            
print("Di quale parola vuoi conoscere il significato?",meme_dict.keys())

parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

if parola in meme_dict.keys():
    print("Il significato della parola è:", meme_dict[parola])
else:
   print("parola non trovata")
