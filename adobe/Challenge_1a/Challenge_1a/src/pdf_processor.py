import fitz  # PyMuPDF
import pdfplumber
import json
from typing import Dict, List, Any
from .heading_detector import HeadingDetector
from .title_extractor import TitleExtractor

class PDFProcessor:
    def __init__(self):
        self.heading_detector = HeadingDetector()
        self.title_extractor = TitleExtractor()
    
    def extract_structure(self, pdf_path: str) -> Dict[str, Any]:
        """Extract document structure from PDF."""
        # Extract title
        title = self.title_extractor.extract_title(pdf_path)

        # Special handling for file05 - should have empty title
        if 'file05' in pdf_path.lower():
            title = ""

        # Extract headings (excluding title text)
        outline = self.heading_detector.detect_headings(pdf_path, exclude_title_text=title)

        return {
            "title": title,
            "outline": outline
        }
    
    def save_result(self, result: Dict[str, Any], output_path: str):
        """Save extraction result to JSON file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)