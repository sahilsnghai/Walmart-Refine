import json
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from app.prompts import walmart_prompt
from app.rules import check_violations
from app.logger import logger

llm = ChatOpenAI(model="gpt-5", temperature=0.7)
walmart_chain = walmart_prompt | llm | StrOutputParser()


def generate_walmart_content(row):
    """Run the LLM chain and return structured output."""
    logger.info("Calling OpenAI chain")

    prompt_inputs = {
        "brand": row.get("brand", ""),
        "product_type": row.get("product_type", ""),
        "attributes": row.get("attributes", ""),
        "current_description": row.get("current_description", ""),
        "current_bullets": row.get("current_bullets", ""),
    }
    try:
        response_text = walmart_chain.invoke(prompt_inputs)
        logger.info("LLM chain completed successfully")
    except Exception as e:
        logger.exception(f"LLM chain failed: {e}")
        response_text = "{}"

    try:
        data = json.loads(response_text or "{}")
    except Exception as e:
        logger.exception(f"Error parsing LLM response: {e}")
        data = {
            "walmart_title": "",
            "key_features_html": "",
            "walmart_description": "",
            "meta_title": "",
            "meta_description": "",
        }

    data["violations"] = check_violations(data)
    return data
