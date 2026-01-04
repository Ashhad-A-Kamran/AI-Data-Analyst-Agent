from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from typing import List, Dict, Any
import pandas as pd
import matplotlib.pyplot as plt
import os
load_dotenv()


class DataAnalysis():
    def __init__(self, user_data_file):
        
        
        if user_data_file 
        self.data = pd.read_csv(user_data_file)
    
    def data_preprocessing(self):
        self.


class IntentRecognitionAgent():
    def __init__(self, query):
        self.query = query
        self.model_name = init_chat_model("llama-3.3-70b-versatile", model_provider="groq", temperature=0.6)


    def _decompose_query(self, query: str) -> List[str]:
            """
            Breaks down a legal query into atomic sub-questions using the LLM.
            Returns a clean list of sub-questions OR the original query on failure.
            """

            system_prompt = """
            You are an assistant that decomposes legal questions.
            Return ONLY a list of simpler sub-questions.
            Format:
            - subquestion 1
            - subquestion 2
            Never give explanations.
            Never add extra text.
            """

            user_prompt = f"Question:\n{query}\n\nReturn sub-questions:"

            payload = {
                "model": self.model_name,
                "prompt": f"{system_prompt}\n\n{user_prompt}",
                "stream": False,
                "options": {"temperature": 0.1, "num_predict": 200}
            }

            try:
                response = requests.post(
                    f"{self.ollama_url}/api/generate",
                    json=payload,
                    timeout=180  # Increased timeout for query decomposition
                )
                response.raise_for_status()

                text = response.json().get("response", "").strip()
                if not text:
                    return [query]

                lines = [line.strip() for line in text.split("\n") if line.strip()]
                sub_questions = []

                for line in lines:
                    # Handle -, *, •
                    if line.startswith(("-", "*", "•")):
                        cleaned = line[1:].strip()
                        if cleaned:
                            sub_questions.append(cleaned)

                    # Handle numbered lists: "1. xxx" or "1) xxx"
                    elif line[0].isdigit():
                        cleaned = line.split(".", 1)[-1].split(")", 1)[-1].strip()
                        if cleaned:
                            sub_questions.append(cleaned)

                return sub_questions if sub_questions else [query]

            except Exception:
                return [query]




    def recognize_intent(self):


        result = self.llm.invoke(self.query)
        print(result.content)

        return result