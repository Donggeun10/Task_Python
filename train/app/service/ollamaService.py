import logging

from ollama import Client

from train.app.configuration.LoggingConfig import log
from train.app.configuration.SecurityConfig import config

model = config('OLLAMA_MODEL')
ollama_host = config('OLLAMA_HOST')
logger = logging.getLogger(__name__)
logger.parent = log

def get_ollama_joke(item : str):
    return ask_ollama_client('please make a joke about ' + item)


def get_spring_boot_version(log_file_name : str):
    logger.debug("log_file_name: ", log_file_name)
    # read file
    consolelog = ""
    with open(log_file_name, 'r', encoding='UTF8') as file:
        consolelog = file.read()

    question = """    
                <|start_header_id|>user<|end_header_id|>
                Answer the following question based only on the provided logs:
                <context>
                    <console_log>
                """
    question += consolelog
    question += """
                    </console_log>
                </context>
                Question:  Please summarize given log and find what kind of frameworks are used  ?
                <|eot_id|>
                
                <|start_header_id|>assistant<|end_header_id|>
                """

    return ask_ollama_client(question)


def summarize(log_file_name : str, stack_trace_file : str):
    print("log_file_name: ", log_file_name)
    # read file
    consolelog = ""
    with open(log_file_name, 'r', encoding='UTF8') as file:
        consolelog = file.read()

    stack_trace = ""
    with open(stack_trace_file, 'r', encoding='UTF8') as file:
        stack_trace = file.read()

    question = """    
                <|start_header_id|>user<|end_header_id|>
                Answer the following question based only on the provided logs:
                <context>
                    <console_log>
                """
    question += consolelog
    question += """
                    </console_log>
                    <stack_trace>
                """
    question += stack_trace
    question += """
                    </stack_trace>
                </context>
                Question:  Please summarize given log and analyze crash causes  ?
                <|eot_id|>
                
                <|start_header_id|>assistant<|end_header_id|>
                """

    return ask_ollama_client(question)


def ask_ollama_client(question : str):

    client = Client(host=ollama_host)
    return client.chat(model=model,
                       messages=[{
                                    'role': 'user',
                                    'content': question,
                                },]
                       )