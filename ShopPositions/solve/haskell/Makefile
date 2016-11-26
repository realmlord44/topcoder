include ../Makefile.common

OUTPUT_D = ../../build/haskell
SOLVER = $(OUTPUT_D)/ShopPositionsSolver
COMPILER = ghc -i$(GETTC_HOME)/include/haskell -outputdir $(OUTPUT_D)

$(SOLVER): ShopPositionsSolver.hs ShopPositions.hs
	$(COMPILER) -o $(SOLVER) $<

main: setup $(SOLVER)

