NC='\033[0m'
echo "${GREEN}updating${NC}"
apt-get update
apt-get install -y libasound2
echo "${GREEN}installing vscode${NC}"
apt install -y spyder
echo "${GREEN}installed vscode${NC}"
