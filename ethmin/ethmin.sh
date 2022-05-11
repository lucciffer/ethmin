nvidia-smi -L

sudo add-apt-repository ppa:ethereum/ethereum
sudo cat /etc/apt/sources.list
sudo apt update
sudo apt install ethereum
wget https://github.com/ethereum-mining/ethminer/releases/download/v0.18.0/ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz

ls
tar -zxvf ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz
cd bin/

echo "Enter worker name: "
read ans
./ethminer -U -P stratum2+tcp://3Kwm7P6y2xyij294BmF9T9efBp2mW8wDYK.$ans@daggerhashimoto.usa-west.nicehash.com:3353
