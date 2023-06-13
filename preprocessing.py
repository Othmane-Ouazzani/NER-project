import csv


def preprocess_data(src, dest):
    with open(src, "r", encoding='utf-8') as f:
        lines = f.readlines()

    with open(dest, "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["sentence_id", "words", "labels"]) # writer.writerow(["sentence_id", "words", "pos", "labels"])

        sentence_num = 0
        for line in lines:
            # strip() supprime les espaces au début et à la fin de la ligne
            line = line.strip()

            if line:
                # Diviser la ligne en mots en utilisant l'espace comme séparateur
                parts = line.split(" ")
                word, tag_complet = parts[0], parts[-1]
                tag = tag_complet

                # Si le tag est B- ou I-, mettre "T" comme POS et extraire le type d'entité
                # if tag_complet.startswith("B-") or tag_complet.startswith("I-"):
                #     tag = tag_complet.split("-")[1]
                #     pos = tag_complet.split("-")[0]

                # else:
                #     pos = ""

                # Écrire la ligne dans le fichier CSV
                writer.writerow([sentence_num, word, tag]) # writer.writerow([sentence_num, word, pos, tag])
            else:
                # Si la ligne est un retour à la ligne, incrémenter le numéro de phrase
                sentence_num += 1
