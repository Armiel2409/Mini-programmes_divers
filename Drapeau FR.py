File = open('flag.ppm','a')

tailleX=int(input("Veuillez rentrer la largeur du drapeau\n"))
tailleY=int(input("Veuillez rentrer la hauteur du drapeau\n"))


File.write("P3\n")
File.write(str(tailleX)+" "+str(tailleY)+"\n")
File.write("255\n")


for i in range(tailleY):
	for j in range(tailleX):
		if(j<tailleX//3):
			File.write("0 0 255 ")
		elif((j>=(tailleX//3))and(j<(2*(tailleX//3)))):
			File.write("255 255 255 ")
		else:
			File.write("255 0 0 ")
File.close()

