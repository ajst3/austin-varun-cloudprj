GREEN='\033[0;32m'
NC='\033[0m'
echo "${GREEN}updating${NC}"
apt-get update
apt-get install -y xterm
echo "${GREEN}installing git${NC}"
apt-get install -y git
echo "${GREEN}installed git${NC}"
