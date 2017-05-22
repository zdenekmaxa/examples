BIN = ethercatch
LIB = 
CFLAGS = -Wall -O -g
CC = gcc

all: 	$(BIN)

ethercatch: ethercatch.o
	$(CC) -o $@ ethercatch.o $(LIB)

ethercatch.o: ethercatch.c 
	$(CC) $(CFLAGS) -c ethercatch.c

clean:
	rm -f *.o *~ $(BIN)






