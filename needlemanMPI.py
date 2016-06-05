from mpi4py import MPI
import sys

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

def needlemanWunch(fila,columna):
  for i in range(fila,largoH2):
    for j in range(columna,largoH1):
      # de la esquina
      match = matrix[i - 1][j - 1] + (1 if hilera1[j - 1] == hilera2[i - 1] else -1);
      # de la derecha
      inserted = (matrix[i][j - 1]) - 1;
      # de arriba
      deleted = (matrix[i - 1][j]) - 1;
      maxScore = max(match, inserted, deleted);
      matrix[i][j] += maxScore;

def ourMPI(comm,size,rank):
	data1 = None
	fila = None
	columna = None
	if (size > largoH2) or (size > largoH1):
		print "No se puede dividir la matrix"
		MPI.Finalize()
		sys.exit()
	else:
		if rank == 0:
			data1 = [i for i in range(largoH2)]
			data2 = [j for j in range(largoH1)]
			fila = [[]for _ in range(size)]
			for i, chunk in enumerate(data1):
				fila[i % size].append(chunk)
			columna = [[]for _ in range(size)]
			for j, chunk in enumerate(data2):
				columna[j % size].append(chunk)
		else:
			if (fila != None) and (columna != None):
				needlemanWunch(fila,columna)
			if ( fila == None) and (columna != None):
				needlemanWunch(1,columna)
			if ( fila != None) and (columna == None):
				needlemanWunch(fila,1)
			else:
				needlemanWunch(1,1)
		data1 = comm.scatter(fila, root=0)
		data2 = comm.scatter(columna, root=0)

def main():
	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()

	llenarMatrix();
	ourMPI(comm,size,rank);
	imprimirMatrix();
		

if __name__ == "__main__":
  sys.exit(main())

