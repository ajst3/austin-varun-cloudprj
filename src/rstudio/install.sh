NC='\033[0m'
echo "${GREEN}updating${NC}"
apt-get update
apt-get install -y r-base
apt-get install -y libasound2
apt-get install -y xterm
apt install -y libnss3
echo "${GREEN}installing rstudio${NC}"
apt install -y ./rstudio-1.3.1093-amd64.deb
echo "${GREEN}installed rstudio${NC}"
