import random
from Bio.SeqUtils import MeltingTemp
from Bio.Seq import Seq
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)



def design_primers(config):
    sequence = config["transcript_sequence"]
    primers = []
    respuesta=[]
    for size in range(config["min_size"], config["max_size"]+ 1):
        for i in range(len(sequence) - size + 1):
            primer = sequence[i:i + size]
            gc_content = (primer.count("G") + primer.count("C")) / len(primer) * 100
            melting_temp = MeltingTemp.Tm_NN(Seq(primer))
            if config["min_size"] <= len(primer) <= config["max_size"] and \
                    config["gc_min"] <= gc_content <= config["gc_max"] and \
                    melting_temp <= config["max_temp"]:
                primers.append(primer)

    for i in primers:
        if i[-1]!="C" and i[-1]!="G":
            respuesta.append(i)

    if len(respuesta)!=0:
        respuesta_5=random.sample(respuesta, 5)
        return respuesta_5
    else:
        primers_5=random.sample(primers, 5)
        return primers_5

designed_primers = design_primers(config)

# Imprimir los primers diseñados
for idx, primer in enumerate(designed_primers):
    melting_temp = MeltingTemp.Tm_NN(Seq(primer))
    print(f"Primer {idx + 1}: {primer}")
    porcentaje =(primer.count('G') + primer.count('C'))/ len(primer) *100
    print(f"porcentaje GC {porcentaje}, size primer: {len(primer)}")
    print(f"melting {melting_temp}")

