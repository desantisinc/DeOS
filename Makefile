export MAKEFLAGS=--no-print-directory

.DEFAULT_GOAL:=all

.PHONY: all build

.SUBLIME_TARGETS: all

include .deosrc

all: build
	@$(PRINT) purple $@ start
	yarn --version
	@$(PRINT) purple $@ stop

build:
	@chmod +x $(PRINT)
	@$(PRINT) yellow $@ start
	@echo $(DEOS_HOST_OS)
	@$(PRINT) yellow $@ stop
