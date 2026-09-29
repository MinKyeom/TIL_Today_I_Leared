import os
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. API Key 설정
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# 2. 문서 로드 (텍스트 파일 예시)
# sample.txt 파일에 참고할 문서 데이터를 넣어두어야 합니다.
loader = TextLoader("sample.txt", encoding="utf-8")
docs = loader.load()

# 3. 문서 분할 (Chunking)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splits = text_splitter.split_documents(docs)

# 4. 임베딩 및 벡터 저장소 생성 (Vector Store)
vectorstore = Chroma.from_documents(
    documents=splits, embedding=OpenAIEmbeddings()
)

# 5. 검색기(Retriever) 생성
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 6. 프롬프트 템플릿 정의
template = """다음 문맥(Context)만을 사용하여 질문에 답변하세요.
답을 모른다면 모른다고 답변하고, 지어내지 마세요.

문맥:
{context}

질문: {question}

답변:"""

prompt = ChatPromptTemplate.from_template(template)

# 7. LLM 모델 정의
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# 문서 결합 함수
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# 8. RAG 체인 구성 (LCEL)
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 9. 질문 및 답변 실행
question = "문서에 적힌 핵심 내용은 무엇인가요?"
response = rag_chain.invoke(question)

print("--- 질문 ---")
print(question)
print("\n--- 답변 ---")
print(response)