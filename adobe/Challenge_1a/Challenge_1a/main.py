import os
from pathlib import Path
from src.pdf_processor import PDFProcessor

def main():
    # Use relative paths for Windows execution
    input_dir = Path("input")
    output_dir = Path("output")
    
    # Create directories if they don't exist
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)
    
    # Initialize processor
    processor = PDFProcessor()
    
    # Find all PDF files in input directory
    pdf_files = list(input_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in input directory")
        return
    
    print(f"Found {len(pdf_files)} PDF files to process")
    
    # Process each PDF
    for pdf_path in pdf_files:
        try:
            print(f"Processing: {pdf_path.name}")

            # Extract structure
            result = processor.extract_structure(str(pdf_path))

            # Debug output
            print(f"  Title: {result.get('title', 'N/A')}")
            print(f"  Found {len(result.get('outline', []))} headings")

            # Save result
            output_path = output_dir / f"{pdf_path.stem}.json"
            processor.save_result(result, str(output_path))

            print(f"✓ Completed: {pdf_path.name} -> {output_path.name}")

        except Exception as e:
            print(f"✗ Error processing {pdf_path.name}: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print("Processing complete!")

if __name__ == "__main__":
    main()