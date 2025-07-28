
🧠 Challenge 1B – Persona-Driven Document Intelligence

Building a Generic, Context-Aware Document Analyst
________________________________________
🔍 Problem Summary

The objective of Round 1B is to build a generic system that intelligently analyzes a collection of PDF documents, and then extracts and ranks the most relevant sections based on a given persona and a clearly defined job-to-be-done.
The challenge is to simulate how a human expert would scan through large volumes of text and select only the information that directly aligns with their context, needs, and intent.
________________________________________
🧠 Logic and Methodology

Our approach addresses this problem using a three-stage pipeline: document parsing, persona understanding, and semantic relevance ranking.
1. Document Structure and Section Extraction
   
Using rule-based PDF parsing logic (evolved from Challenge 1A), the system:
•	Scans each document to identify titles, headings, and structured content sections.
•	Extracts each section's metadata: document name, page number, heading text, and full paragraph content.
•	Organizes these sections into a uniform internal structure for further analysis.
This stage ensures all documents, regardless of formatting, are broken down into comparable and analyzable chunks of information.
________________________________________
2. Persona Understanding via Embedding
   
The persona input is a combination of:
•	Role (e.g., “Investment Analyst”)
•	Task/Job-to-be-Done (e.g., “Analyze revenue trends for Q4”)
To simulate contextual understanding:
•	The system concatenates the role and task into a single descriptive string.
•	This description is transformed into a dense semantic embedding using a lightweight sentence transformer model (e.g., all-MiniLM-L6-v2).
•	This embedding represents the intent and focus of the user.
________________________________________
3. Semantic Similarity & Section Ranking
   
Each extracted section from the documents is:
•	Converted into its own semantic embedding (title + content).
•	Compared against the persona embedding using cosine similarity to measure semantic closeness.
Sections with the highest similarity scores are considered most relevant and are:
•	Assigned a numerical importance_rank.
•	Filtered based on relevance thresholds and content quality.
This allows the system to prioritize sections that semantically align with what the persona is trying to achieve.
________________________________________
4. Subsection Refinement and Filtering

To improve granularity:
•	Top-ranked sections are further broken down into smaller paragraphs or logical units.
•	Each subsection is individually scored against the persona embedding.
•	Subsections are selected only if they exceed a minimum relevance threshold and contain meaningful content (e.g., more than 100 characters).
This produces high-precision, actionable insights, giving the user not only where to look (sections) but also what exactly to read (subsections).
________________________________________
🎯 Output Structure

The final JSON output contains:
🔹 Metadata:
•	Persona and task details
•	List of processed documents
•	Timestamp of execution
🔹 Sections:
•	List of relevant sections with:
o	Document name
o	Section title
o	Page number
o	Importance ranking score
🔹 Subsections:
•	Refined text snippets with:
o	Source document
o	Page number
o	Relevance score
________________________________________
✅ How the Approach Meets Constraints

Constraint	Compliance	Explanation
CPU-only Execution	✅	No GPU required; model runs efficiently on CPU
Model Size ≤ 1GB	✅	Uses ~384MB MiniLM transformer
< 60 sec for 3–5 Docs	✅	Fast embedding and ranking operations
Offline Execution	✅	No internet dependency; runs in isolated containers
AMD64 Docker Compatibility	✅	Fully Dockerized for linux/amd64
Generic to Domains and Personas	✅	Persona embedding + semantic scoring ensures adaptability
________________________________________
🔁 Why This Logic Works

•	Generic & Scalable: Works for any domain, any role, and any task.
•	Human-Like Prioritization: Simulates how a human expert filters content based on context.
•	Precise Output: Delivers both overview (sections) and deep insights (subsections).
•	Deterministic & Auditable: Every decision is traceable, explainable, and reproducible.
________________________________________

