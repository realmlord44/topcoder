include ../Makefile.common

OUTPUT_D =../../build/go
SOLVER = $(OUTPUT_D)/ShopPositionsSolver

$(SOLVER): ShopPositionsSolver.go ShopPositions/ShopPositions.go
	export GOPATH="$$GOPATH:$(GETTC_HOME)/include/go" \
		&& go build -o $(SOLVER) ShopPositionsSolver.go 

main: setup $(SOLVER)
