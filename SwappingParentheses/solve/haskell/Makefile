include ../Makefile.common

OUTPUT_D = ../../build/haskell
SOLVER = $(OUTPUT_D)/SwappingParenthesesSolver
COMPILER = ghc -i$(GETTC_HOME)/include/haskell -outputdir $(OUTPUT_D)

$(SOLVER): SwappingParenthesesSolver.hs SwappingParentheses.hs
	$(COMPILER) -o $(SOLVER) $<

main: setup $(SOLVER)

