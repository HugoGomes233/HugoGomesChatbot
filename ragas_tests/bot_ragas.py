from ragas import EvaluationDataset
from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness
from .ragas_dataset import sample_queries, expected_responses
from bot_core import load_pdf, create_vectorstore, create_qa_chain


dataset = []

docs = load_pdf()
vectorstore = create_vectorstore(docs)
qa_chain , llm = create_qa_chain(vectorstore)


for query, reference in zip(sample_queries, expected_responses):
    response = qa_chain.invoke(query)
    dataset.append(
        {
            "user_input": query,
            "retrieved_contexts": [rdoc.page_content for rdoc in response["source_documents"]],
            "response": response["result"],
            "reference": reference,
        }
    )

evaluation_dataset = EvaluationDataset.from_list(dataset)

evaluator_llm = LangchainLLMWrapper(llm)

result = evaluate(dataset=evaluation_dataset,metrics=[LLMContextRecall(), Faithfulness(), FactualCorrectness()],llm=evaluator_llm)

print(f"Overall Result : {result}")

for i, row in zip(sample_queries,result.scores):
    print(f"Pergunta {i}: {row}")