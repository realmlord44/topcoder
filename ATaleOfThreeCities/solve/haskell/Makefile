include ../Makefile.common

OUTPUT_D = ../../build/haskell
SOLVER = $(OUTPUT_D)/ATaleOfThreeCitiesSolver
COMPILER = ghc -i$(GETTC_HOME)/include/haskell -outputdir $(OUTPUT_D)

$(SOLVER): ATaleOfThreeCitiesSolver.hs ATaleOfThreeCities.hs
	$(COMPILER) -o $(SOLVER) $<

main: setup $(SOLVER)

