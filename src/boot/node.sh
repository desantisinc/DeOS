MAINTAINER "atd@bitcoin.sh"
RUN "curl -sL $NODE_INSTALL | sudo -E bash -"
RUN "apt-get -y install nodejs $BOOT_DEBUG"
EXIT_SUCCESS
EXIT_FAILURE
