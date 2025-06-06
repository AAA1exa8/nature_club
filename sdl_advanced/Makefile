# Compiler and flags
CC       := gcc
CFLAGS   := -std=c17 -Wall -Wextra -Wpedantic -Werror -Wshadow -Wno-unused-parameter -O2
PKGCONFIG	:= pkg-config
LDFLAGS  := $(shell $(PKGCONFIG) --libs sdl3)

# Output binary name and folders
TARGET_DIR := bin
OBJ_DIR    := obj
SRC_DIR    := src
TARGET     := $(TARGET_DIR)/main

# Source and object files
SRCS := $(wildcard $(SRC_DIR)/*.c)
OBJS := $(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRCS))

# Phony targets
.PHONY: all clean rebuild debug dirs

# Default target
all: clean dirs $(TARGET)

# Link object files into final binary
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $@ $(LDFLAGS)
	@echo "Build complete! Binary is in $(TARGET)"

# Compile source files to object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

# Ensure directories exist
dirs:
	@mkdir -p $(OBJ_DIR)
	@mkdir -p $(TARGET_DIR)

# Clean build artifacts
clean:
	rm -rf $(OBJ_DIR) $(TARGET_DIR)

# Clean and rebuild
rebuild: clean all

# Debug build
debug: CFLAGS += -g -O0
debug: rebuild

