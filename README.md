# Sae Images

## Partie A

### A.0) 
Il faut modifiez la taille du fichier dans okteta: 99 passe a 9A

### A.1)
![Image réponses okteta](A1.png)

### A.2)
![Image réponses okteta](A2.png)

### A.3) 74+28=102
#### 1) Toujours 24 bits par pixels -> car encore codée a 0x18
#### 2) 0x30 donc 48 octets
#### 3) Il n'y a pas de compression
#### 4) Le codage des pixels n'a pas changé

### A.4)
#### 1) 1bits par pixels
#### 2) 0x10 donc 16 octets
#### 3) Oui il y'a une compression utilisé
#### 4) Ils sont codée juste apres l'entete du fichiers, sur 4 octets
#### 5) Il y'a deux couleurs dans la palette, le rouge est blanc qui se situe au début -> 0x00 0x00 0xFF et 0xFF 0xFF 0xFF
#### 6) Oui le codage des pixels a changé, maintenant on code sur 4 octet en modifiant seulement le premier quartet du deuxieme octet, 
#### 7) Pour changer la couleur rouge en couleur bleue, quand on regles les couleurs au début j'ai modifié le rouge 0x00 0x00 0xFF en bleue 0xFF 0x00 0x00
#### 8) Pour inversez le damier j'ai échanger la place des couleurs bleu et blanche dans les parametre de la palette, j'ai d'abord mis le blanc puis le bleue
#### 9)
[Image réponses okteta](A).png)
#### 11) a l'adresse 0x29
#### 12) la 13 couleurs = C
#### 13) ?? 76 ?
#### 14) on rajoute des E au début (E car 15 couleurs est bleu)
#### 15)

### A.5)
#### 2)
inversion 4 en -4
04 00 00 00 en FC FF FF FF
0100 0000 0000 0000 0000 0000 0000 0000 en 1111 1100 1111 1111 1111 1111 1111 1111

#### 3) inversion de A9 01 00 00 en 57 FE FF FF
1010 1001 0000 0001 0000 0000 0000 0000 en 0101 0111 1111 1110 1111 1111 1111 1111
[Image réponses okteta](A5.png)

### A.6) 
#### 1) poid de 60 04 00 00 donc 1120 octets
il a augmenté car on est passer a une palette de 256 couleurs (00 01 00 00) et qu'on code maintenant chaque pixels sur 8 bits
#### 2) on peut trouver a A0  codé sur 4 octet l'adresse de début ( ici 36 04 00 00)
#### 3) [Image réponses okteta](A6.png)
on lit les octets deux par deux, le premier est le nombre d'occurence de la couleurs qui est définit dans le deuxieme octet
00 représente le blanc et 01 représente le rouge
donc si on a 01 00 on aura un pixels rouge et si on a 01 01 on aura un pixel blanc
on peut imaginer que si il y'aurai eu 03 01 il y aurait eu 3 pixels blanc d'affilé
ensuite quand dans le premier octet il y'a 0 occurence de couleurs donc 00 et dans le second 00 aussi alors c'est une fin de ligne, par contre si dans le premier il y'a encore 00 et dans le second 01 alors c'est une fin de bitmap donc fin d'image
donc si on lit notre image ci-dessus on a :
01 00 01 01 01 00 01 01 00 00 - 1 rouge, 1 blanc, 1 rouge, 1 blanc, fin de ligne
01 01 01 00 01 01 01 00 00 00 01 00 01 01 01 00 - 1 blanc, 1 rouge, 1 blanc , 1 rouge, fin de ligne, 1 rouge, 1 blanc, 1 rouge
01 01 00 00 01 01 01 00 01 01 01 00 00 00 00 01 - 1 blanc, fin de ligne, 1 blanc, 1 rouge, 1 blanc,1 rouge, fin de ligne, fin d'image

### A.7)
#### 1) le poid de l'image est 1102 octets
le poid est moins grand que précedemment car dans cette image il y'a des suite de pixels qui ont la meme couleurs, donc la compression en RLE prend tout son sens car elle permet de coder ça plus facilement 
#### 2) [Image réponses okteta](A7.png)
04 01 00 00 04 00 00 00 04 00 - 4 blanc, fin de ligne, 4 rouge, fin de ligne, 4 rouge
00 00 01 01 01 00 01 01 01 00 00 00 00 01 - fin de ligne, 1 blanc, 1 rouge, 1 blanc, 1 rouge, fin de ligne, fin d'image

### A.8)[Image réponses okteta](A8.png)
j'ai modifié la premiere ligne afin d'obtenir 2 blanc, 1 rouge, 1 blanc donc 
je suis passer de 04 01 00 00 a 02 01 01 00 01 01 00 00
j'ai donc rajouté 4 octets donc je suis aller modifier la taille du fichier de 4E 04 00 00 a 52 04 00 00  

### A.9)[Image réponses okteta](A9_1.png)
J'ai d'abord rajouter le bleu et vert dans ma palette de couleurs donc FF 00 00 et 00 FF 00 qui seront donc la couleurs 02 et 03
[Image réponses okteta](A9_2.png)
j'ai ensuite modifier les valeurs héxadecimal de l'image pour que les pixels ait la bonne couleurs

### A.10)
[Image réponses okteta](A10.png)
Pour réduire le nombre de couleurs on change le nombre de couleurs de la palette de 256 a 4 donc : 
00 01 00 00 a 04 00 00 00
ensuite on peut enlever tout les 00 00 00 00 qui correspondait aux couleurs noirs de la palette de 256 couleurs, enfin il nous reste a changer la taille du fichier en fonction du nouveau poids du fichier donc ici 106 soit 6A et enfin mettre dans le header la nouvelle adresse où l'image commence donc 46 00 00 00


## Partie B

### B.1)
[Image réponses VScode](B1_1)![Image Rendu](B1_2)

### B.2)
[Image réponses VScode](B2_1)![Image Rendu](B2_2)

### B.3)
[Image réponses VScode](B3_1)![Image Rendu](B3_2)

### B.4)
[Image réponses VScode](B4_1)![Image Rendu](B4_2)

### B.5)
[Image réponses VScode](B5_1)![Image Rendu](B5_2)

[Image réponses VScode](B6_1)![Image Rendu](B6_2)