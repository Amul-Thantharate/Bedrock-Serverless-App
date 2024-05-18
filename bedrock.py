import os
import boto3
import dotenv 
from langchain.chains import ConversationChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
dotenv.load_dotenv()

def bedrock_chain():
    """
    Creates and returns a conversation chain using the Bedrock library.

    This function sets up a conversation chain with a prompt template, a language model, and a memory buffer.
    The conversation chain can be used to generate responses to user inputs based on the provided prompt template.

    Returns:
        ConversationChain: The conversation chain object that can be used to generate responses.

    Raises:
        KeyError: If the AWS_PROFILE environment variable is not set.

    Example usage:
        conversation = bedrock_chain()
        response = conversation.generate_response("Hello")
        print(response)
    """
    # profile = os.environ["AWS_PROFILE"]


    # Rest of the code...
def bedrock_chain():
    # profile = os.environ["AWS_PROFILE"]

    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    )

    titan_llm = Bedrock(
        model_id="amazon.titan-text-express-v1", client=bedrock_runtime
    )
    titan_llm.model_kwargs = {"temperature": 0.5, "maxTokenCount": 700}

    prompt_template = """System: The following is a friendly conversation between a knowledgeable helpful assistant and a customer.
    The assistant is talkative and provides lots of specific details from it's context.

    Current conversation:
    {history}

    User: {input}
    Bot:"""
    PROMPT = PromptTemplate(
        input_variables=["history", "input"], template=prompt_template
    )

    memory = ConversationBufferMemory(human_prefix="User", ai_prefix="Bot")
    conversation = ConversationChain(
        prompt=PROMPT,
        llm=titan_llm,
        verbose=True,
        memory=memory,
    )

    return conversation 

def run_chain(chain, prompt):
    num_tokens = chain.llm.get_num_tokens(prompt)
    return chain({"input": prompt}), num_tokens


def clear_memory(chain):
    return chain.memory.clear()