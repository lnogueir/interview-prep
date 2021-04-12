BIN := bin
STD := -std=c++17

test: all
	./bin/main

all: bin heaps main

heaps: heaps.hpp
	g++ -c $(STD) $^ -o $(BIN)/$@.o

main: main.cpp
	g++ $(STD) $^ -o $(BIN)/$@

bin:
	mkdir -p $(BIN)

clean:
	rm -rf bin
