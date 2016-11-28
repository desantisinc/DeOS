include .deosrc

all: vm #build; @($(DEOS) && echo)

app:; electron ./app/

build: chmod check

check: deos.check; @(echo)

chmod:; (chmod +x $(PRINT) $(DEOS))

clean:; -(rm -rf node_modules/)

down:; (vagrant destroy DeVM)

install:; (yarn global add electron)

ssh:; (vagrant ssh -c $(VMCMD) DeVM)

vm: deos.vm

yarn:; @(yarn all)
