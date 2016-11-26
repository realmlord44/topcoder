include ../Makefile.common

OUTPUT_D =../../build/cpp
SOLVER = $(OUTPUT_D)/ATaleOfThreeCitiesSolver
COMPILER = g++ -std=gnu++0x -I$(GETTC_HOME)/include/cpp

$(SOLVER): ATaleOfThreeCitiesSolver.cpp ATaleOfThreeCities.cpp
	$(COMPILER) -o $(SOLVER) $<

main: setup $(SOLVER)
