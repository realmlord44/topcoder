include ../Makefile.common

OUTPUT_D =../../build/go
SOLVER = $(OUTPUT_D)/ATaleOfThreeCitiesSolver

$(SOLVER): ATaleOfThreeCitiesSolver.go ATaleOfThreeCities/ATaleOfThreeCities.go
	export GOPATH="$$GOPATH:$(GETTC_HOME)/include/go" \
		&& go build -o $(SOLVER) ATaleOfThreeCitiesSolver.go 

main: setup $(SOLVER)
