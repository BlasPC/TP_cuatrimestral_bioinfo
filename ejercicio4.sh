#!/bin/bash

# Define input_file con el archivo que contiene la secuencia de nucleotidos de nuestro Ej. 1
input_file="nucleotidos.fasta"
# Nombre del archivo de salida
output_file="resultados_prosite.txt"

# Calcula los ORF y obtiene las secuencias de proteínas
transeq -sequence $input_file -outseq protein_sequences.fasta

# Define input_fasta donde se va a guardar la secuencia de proteinas traducida por EMBOSS con el cual va a realizar el análisis de dominios
input_fasta="proteins_sequences.fasta"

# Descarga el archivo PROSITE (prosite.dat)
if [ ! -f prosite.dat ]; then
  wget ftp://ftp.expasy.org/databases/prosite/prosite.dat
fi

# Descarga el archivo PROSITE (prosite.doc)
if [ ! -f prosite.doc ]; then
  wget ftp://ftp.expasy.org/databases/prosite/prosite.doc
fi

# Redirecciona el default output a mi carpeta asi tengo el permiso de edicion
export EMBOSS_DATA="./"

# Analiza los dominios de la secuencia de aminoácidos utilizando PROSITE
prosextract -prositedir ./

# Analiza mi secuencia del archivo input y la guarda en el output
patmatmotifs -full -sequence $input_fasta -outfile $output_file

# Muestra los resultados del archivo creado y luego filtra y muestra solo los Motif generados con mi secuencia
cat $output_file
cat $output_file | grep Motif