import hashlib  # creates cryptographic hash of the blocks
import datetime as date # creates timestamps at each block
import uuid # creates unique IDs
from pprint import pprint
import json
import re
import xmltodict
from llama_cpp import Llama

# load LLM
llm = Llama(
      model_path="/home/missvector/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
      n_ctx=2048, # context window
)

# load knowledge base
with open('tbl.ttl') as f:
    KB = xmltodict.parse(f.read())

class Block:
    def __init__(self, data, blockId="", previousBlockHash=""):
        """
        args:
        :blockId: unique block identifier, the position of the block in the chain
        :previousBlockHash: the cryptographic hash of the previous block in the chain
        :timestamp: the time at which the block was added in the chain
        :data: the data stored in the block
        :hash: the cryptographic hash of the current block
        """
        self.blockId = blockId
        self.previousBlockHash = previousBlockHash
        self.timestamp = date.datetime.now()
        self.data = data
        self.hash = self.get_hash()

    def get_hash(self):
        """
        calculate hash using sha256
        :return: hash for the current block
        """
        hash_str = str(self.blockId) + str(self.timestamp) + str(self.data) + str(self.previousBlockHash)
        return hashlib.sha256(hash_str.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        """
        :chain: empty chain with one root block
        """
        self.chain = [self.root()]

    def root(self):
        """
        create empty root block
        :return: empty root block
        """
        return Block(data='Root', blockId=0, previousBlockHash=0)

    def add_block(self, block):
        """
        add a new block to the chain
        :block: Block object
        """
        # calculate hash
        block.previousBlockHash = self.top_block().hash
        block.hash = block.get_hash()

        # calculate block ID
        block.blockId = self.top_block().blockId + 1

        # update log
        if block.data != "Root" and self.top_block().data != "Root":
            print(block.data['log'])
            block.data['log'] += self.top_block().data['log']

        # TODO: if validate() == True:
        self.chain.append(block)

    def top_block(self):
        """
        get a top block in the chain
        :return: top block in the chain
        """
        return self.chain[-1]

    def validate(self):
        """
        TODO guardrail checks: injections and hallucinations
        :return:
        """
        pass

class Data():
    def __init__(self, userCard, currentPromptTokens, guardrail):
        """
        :userCard: user data
        :log: machine-human interaction history
        :currentPromptTokens: tokenized prompt
        :generatedResult: LLM generation result
        :extractedInfo: RAG retrieval output
        :guardrail: relevant guardrail in XML
        """
        self.userCard = userCard
        self.guardrail = guardrail
        self.currentPromptTokens = currentPromptTokens
        self.extractedInfo = self.retrieval()
        self.generatedResult = self.generate()
        self.data = dict()

    def build(self):
        self.data['userCard'] = self.userCard
        self.data['log'] = self.log()
        self.data['currentPromptTokens'] = self.currentPromptTokens
        self.data['generatedResult'] = self.generatedResult
        self.data['extractedInfo'] = self.extractedInfo
        self.data['guardrail'] = self.guardrail
        return self.data

    def retrieval(self):
        # word-level tokenization
        tokens = re.sub(r'\W', ' ', self.currentPromptTokens.lower())
        tokens = tokens.split()
        # exact match
        for token in tokens:
            if token in str(KB) and len(token) > 5:
                return re.findall(r"http.*?"+token+".*?#", str(KB))[0]

    def generate(self):
        output = llm(
            f"Q: {self.currentPromptTokens} A: ",  # Prompt
            max_tokens=64,  # Generate up to 64 tokens, set to None to generate up to the end of the context window
            stop=["Q:", "\n"],  # Stop generating just before the model would generate a new question
            #echo=True  # Echo the prompt back in the output
        )  # Generate a completion, can also call create_completion

        return output

    def log(self):
        return f"USER:': {self.currentPromptTokens}, 'SYSTEM:': {self.generatedResult['choices'][0]['text']}"

class userCard():
    def __init__(self, age, interests, accessibilityTools, toneOfVoice):
        """
        :userId: unique user identifier (ID)
        :age: user age (int)
        :interests: list of interests (list)
        :accessibilityTools: list of relevant accessiblity settings (dict)
        :toneOfVoice: list of relevant tone of voice settings (dict)
        """
        self.userId = self.generate_id()
        self.age = age
        self.interests = interests
        self.accessibilityTools = self.parse_tools(accessibilityTools)
        self.toneOfVoice = self.parse_tone(toneOfVoice)
        self.card = dict()

    def generate_id(self):
        """
        generates unique user identifier
        :return: user ID
        """
        return uuid.uuid4()

    def parse_tools(self, accessibilityTools):
        """
        :return: accessibilityTools (dict)
        """
        return {"textToSpeech": accessibilityTools.textToSpeech, "simplifiedLanguage": accessibilityTools.simplifiedLanguage, "enhancedVisualization": accessibilityTools.enhancedVisualization}

    def parse_tone(self, toneOfVoice):
        """
        :return: toneOfVoice (dict)
        """
        return {"formality": toneOfVoice.formality, "positivity": toneOfVoice.positivity, "humor": toneOfVoice.humor}

    def build(self):
        self.card['userId'] = self.userId
        self.card['age'] = self.age
        self.card['interests'] = self.interests
        self.card['accessibilityTools'] = self.accessibilityTools
        self.card['toneOfVoice'] = self.toneOfVoice
        return self.card

class accessibilityTools():
    def __init__(self, textToSpeech, simplifiedLanguage, enhancedVisualization):
        """
        :textToSpeech: (Bool)
        :simplifiedLanguage: (Bool)
        :enhancedVisualization: (Bool)
        """
        self.textToSpeech = textToSpeech
        self.simplifiedLanguage = simplifiedLanguage
        self.enhancedVisualization = enhancedVisualization

class toneOfVoice():
    def __init__(self, formality, positivity, humor):
        """
        :formality: (str)
        :positivity: (str)
        :humor: (str)
        """
        self.formality = formality
        self.positivity = positivity
        self.humor = humor

# create the chain
blockchain = Blockchain()

# import userCard values from json
with open('data.json') as f:
    user_data = json.load(f)
# get age info
age = user_data['age']
# parse interests string
interests = user_data['interests'].lower()
interests = re.sub(r'\W', ' ', interests)
interests = interests.split()
# parse Tools data
accessibilityTools = accessibilityTools(textToSpeech=user_data["speech"],
                                        simplifiedLanguage=user_data["language"],
                                        enhancedVisualization=user_data["visuals"])
# pase Tone-of-Voice data
toneOfVoice = toneOfVoice(formality=user_data["formality"],
                          positivity=user_data["positivity"],
                          humor=user_data["humor"])
# form userCard
userCard = userCard(age, interests, accessibilityTools, toneOfVoice).build()

generatedResult = ""
extractedInfo = ""
log = ""

# define guardrail
with open('guardrail.xml') as f:
    guardrail = xmltodict.parse(f.read())

# create a block
sample_block = Block(Data(userCard, "What is inclusion?", guardrail).build())
sample_block_ = Block(Data(userCard, "Should I learn sign language to study in an inclusive school?", guardrail).build())
sample_block__ = Block(Data(userCard, "Should I learn foreign language to study in an inclusive school?", guardrail).build())

# add a block
blockchain.add_block(sample_block)
blockchain.add_block(sample_block_)
blockchain.add_block(sample_block__)

for block in blockchain.chain:
    print('Block ID:', str(block.blockId))
    print('Previous Hash:', str(block.previousBlockHash))
    print('Timestamp:', str(block.timestamp))
    print('Data:')
    pprint(block.data)
    print('Hash:', block.hash)
    print()
