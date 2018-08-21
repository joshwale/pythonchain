import hashlib
import json

class Block(object):
    def __init__(self,index,timestamp,data,previousHash=""):
        self.index=index;
        self.timestamp=timestamp;
        self.data=data;
        self.previousHash=previousHash;
        self.hash="";

    def calculateHash(self):
        return str(hashlib.sha256((str(self.index)+self.previousHash+self.timestamp+str(self.data)).encode("utf-8")).hexdigest());

class Blockchain(object):
    def __init__(self):
        self.chain=[self.createGenesisBlock()];

    def createGenesisBlock(self):
        return Block(0,"01/01/18","Genesis block","0");

    def getLatestBlock(self):
        return self.chain[-1];

    def addBlock(self,newBlock):
        newBlock.previousHash=self.getLatestBlock().hash;
        newBlock.hash=newBlock.calculateHash();
        self.chain.append(newBlock);

    def isChainValid(self):
        i=1
        chain=self.chain
        while(i<len(chain)):
            currentBlock=chain[i]
            previousBlock=chain[i-1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False

            if currentBlock.previousHash !=previousBlock.hash:
                return False
            i+=1

            return True

    def display(self):
        for block in self.chain:
            print("Block "+str(block.index));
            print("timestamp :"+block.timestamp+" ");
            print("data :"+str(block.data));
            print("previousHash :"+block.previousHash);
            print("hash :"+block.hash+" \n");

if __name__=="__main__":
    savCoin=Blockchain();
    savCoin.addBlock(Block(1,"10/07/2017",{"amount":4}));
    savCoin.addBlock(Block(2,"12/07/2017",{"amount":10}));    
         
    savCoin.display()

    print("Is chain valid:" +str(savCoin.isChainValid()))

    savCoin.chain[1].data={"Amount":100}

    print("Is chain valid:" +str(savCoin.isChainValid()))
    
        
        
      
