import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Add the Challenge 1A source directory to the path
sys.path.append(str(Path(__file__).parent.parent / "Challenge_1a" / "Challenge_1a"))

from src.pdf_processor import PDFProcessor
# TODO: The following imports need to be implemented for Challenge 1B functionality
# from src.persona_analyzer import PersonaAnalyzer
# from src.section_ranker import SectionRanker
# from src.embedding_manager import EmbeddingManager

class Challenge1BProcessor:
    """Processor for Challenge 1B: Persona-Driven Document Intelligence."""
    
    def __init__(self):
        """Initialize the processor with all required components."""
        self.pdf_processor = PDFProcessor()
        # TODO: Implement the following components for Challenge 1B functionality
        # self.embedding_manager = EmbeddingManager()
        # self.persona_analyzer = PersonaAnalyzer(self.embedding_manager)
        # self.section_ranker = SectionRanker(self.embedding_manager)
    
    def process_collection(self, input_file_path: str, output_file_path: str):
        """Process the PDF collection based on the input configuration."""
        
        # Load input configuration
        with open(input_file_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Extract collection directory from input file path
        collection_dir = Path(input_file_path).parent
        
        print("Challenge 1B: Persona-Driven Document Intelligence")
        print(f"Collection directory: {collection_dir}")
        print(f"Persona: {config['persona']['role']}")
        print(f"Task: {config['job_to_be_done']['task']}")
        print(f"Documents to process: {len(config['documents'])}")
        
        # Process all PDFs and extract sections
        all_sections = []
        processed_documents = []
        
        for doc_info in config['documents']:
            pdf_path = collection_dir / "pdf" / doc_info['filename']
            
            if not pdf_path.exists():
                print(f"Warning: {doc_info['filename']} not found, skipping...")
                continue
                
            try:
                print(f"Processing: {doc_info['filename']}")

                # Extract structure using available PDFProcessor method
                result = self.pdf_processor.extract_structure(str(pdf_path))

                # TODO: Implement extract_sections_with_text method in PDFProcessor
                # For now, create basic sections from the outline
                sections = []
                if 'outline' in result:
                    for heading in result['outline']:
                        section = {
                            'title': heading.get('text', ''),
                            'level': heading.get('level', 'H1'),
                            'page': heading.get('page', 1),
                            'content': '',  # TODO: Extract actual content
                            'document': doc_info['filename']
                        }
                        sections.append(section)
                        all_sections.append(section)

                processed_documents.append(doc_info['filename'])
                print(f"  ✓ Extracted {len(sections)} sections")
                
            except Exception as e:
                print(f"  ✗ Error processing {doc_info['filename']}: {str(e)}")
        
        if not all_sections:
            print("No sections extracted from any documents!")
            return
        
        print(f"\nTotal sections extracted: {len(all_sections)}")
        
        # TODO: Implement persona analysis and section ranking
        # For now, create a basic output structure without persona analysis
        print("Creating basic output structure...")
        basic_results = {
            'metadata': {
                'persona': config['persona'],
                'task': config['job_to_be_done']['task'],
                'documents': processed_documents,
                'total_sections': len(all_sections),
                'timestamp': datetime.now().isoformat()
            },
            'sections': all_sections[:10],  # Return first 10 sections as placeholder
            'subsections': []  # TODO: Implement subsection extraction
        }

        # Save results
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(basic_results, f, indent=2, ensure_ascii=False)

        print(f"✓ Basic processing complete: {output_file_path}")
        print(f"Extracted {len(all_sections)} total sections from {len(processed_documents)} documents")
        print("Note: Persona analysis and intelligent ranking not yet implemented")
    
    def _adapt_config_format(self, config: dict) -> dict:
        """Adapt Challenge 1B config format to work with existing components."""
        return {
            "persona": config["persona"],
            "job_to_be_done": config["job_to_be_done"]["task"]
        }


def main():
    """Main entry point for Challenge 1B processing."""
    
    # Define paths
    input_file = Path("collection_1/challenge1b_input.json")
    output_file = Path("collection_1/challenge1b_output.json")
    
    # Check if input file exists
    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        return
    
    # Create processor and run
    processor = Challenge1BProcessor()
    processor.process_collection(str(input_file), str(output_file))


if __name__ == "__main__":
    main()
