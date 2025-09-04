import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course!")
    # print(os.environ.get("OPENAI_API_KEY"))

    information = """
        Elon Musk is an asshole from South Africa. He likes to make up stuff and lie to investors.
        He likes to piss in his pants.
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    print(response.content)

if __name__ == "__main__":
    main()
