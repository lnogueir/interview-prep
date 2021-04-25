BIN := bin
STD := -std=c++17
DS_PATH := data-structures

test: all
	./bin/playground

all: bin heaps playground

heaps: $(DS_PATH)/Heaps.hpp
	g++ -c $(STD) $^ -o $(BIN)/$@.o

playground: playground.cpp
	g++ $(STD) $^ -o $(BIN)/$@

bin:
	mkdir -p $(BIN)

clean:
	rm -rf bin
