include ../Makefile.common

OUTPUT_D =../../build/go
SOLVER = $(OUTPUT_D)/SwappingParenthesesSolver

$(SOLVER): SwappingParenthesesSolver.go SwappingParentheses/SwappingParentheses.go
	export GOPATH="$$GOPATH:$(GETTC_HOME)/include/go" \
		&& go build -o $(SOLVER) SwappingParenthesesSolver.go 

main: setup $(SOLVER)
