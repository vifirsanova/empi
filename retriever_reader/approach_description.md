# 2-staged Retriever-Reader Approach to Information Retrieval (IR) Question Answering (QA)

## Model Structure
**Input:** question in natural language
1. **Document Retriever** selects *n* potentially relevant documents from the source 
2. **Machine Reading Comprehension (MRC) Module** processes documents to extract the answer

**Output:** extracted answer

[The structure of IR QA](image_url)

## Challenges:
* The MRC performance us bounded by the Retriever performance
* Most studies focuse on the MRC algorithms  
