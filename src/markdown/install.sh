GREEN='\033[0;32m'
NC='\033[0m'
echo "${GREEN}updating${NC}"
apt-get update 
echo "${GREEN}installing markdown${NC}"
# apt-get install -y markdown
apt-get install -y retext
echo "${GREEN}installed markdown${NC}"
