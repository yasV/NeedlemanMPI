
need: needleman.py
	python needleman.py h1.txt h2.txt
	

needMPI: needlemanMPI.py
	mpiexec -n 3 python needlemanMPI.py h1.txt h2.txt

