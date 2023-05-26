# Compiler options
CXX = g++
CXXFLAGS = -Wall -g
LDFLAGS = -lraylib -lGL -lm -lpthread -ldl -lrt -lX11
 
# Source files
SOURCES = $(wildcard *.cpp)
OBJECTS = $(SOURCES:.cpp=.o)

# Output binary
TARGET = program

# Default target
all: $(TARGET)
	./program

# Linking the binary
$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $^ -o $@

# Compiling source files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -c $< -o $@

# Clean
clean:
	$(RM) $(OBJECTS) $(TARGET)

# Phony targets
.PHONY: all clean
