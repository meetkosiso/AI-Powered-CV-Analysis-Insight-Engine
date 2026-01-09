from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template("""
Answer using only the provided context. Cite sources.

Context: {context}

Question: {input}
""")
