include ../Makefile.common

OUTPUT_D =../../build/cpp
SOLVER = $(OUTPUT_D)/ShopPositionsSolver
COMPILER = g++ -std=gnu++0x -I$(GETTC_HOME)/include/cpp

$(SOLVER): ShopPositionsSolver.cpp ShopPositions.cpp
	$(COMPILER) -o $(SOLVER) $<

main: setup $(SOLVER)
