import sys
#from mpi4py import MPI

#hileras
with open(sys.argv[1], 'r') as getHilera1:
  hilera1 = getHilera1.read()
with open(sys.argv[2], 'r') as getHilera2:
  hilera2 = getHilera2.read() 
  
#largo de las hileras 
largoH1 = len(hilera1) + 1;
largoH2 = len(hilera2) + 1;

#Creo la matrix
matrix = [[0 for x in range(largoH1)] for y in range(largoH2)];

def llenarMatrix():
    #Lleno la fila y columna uno con el index
    for i in range(largoH2):
      matrix[i][0] = -i;
    for j in range(largoH1):
      matrix[0][j] = -j;

def imprimirMatrix():
    print "Mejor Puntaje Obtenido de la comparacion>",matrix[largoH2-1][largoH1-1];

def needlemanWunch():
  for i in range(1,largoH2):
    for j in range(1,largoH1):
      # de la esquina
      match = matrix[i - 1][j - 1] + (1 if hilera1[j - 1] == hilera2[i - 1] else -1);
      # de la derecha
      inserted = (matrix[i][j - 1]) - 1;
      # de arriba
      deleted = (matrix[i - 1][j]) - 1;
      maxScore = max(match, inserted, deleted);
      matrix[i][j] += maxScore;

def main():
    llenarMatrix();
    needlemanWunch();
    imprimirMatrix();

if __name__ == "__main__":
  sys.exit(main())