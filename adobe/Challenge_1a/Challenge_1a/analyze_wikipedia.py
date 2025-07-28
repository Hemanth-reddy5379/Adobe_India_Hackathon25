#!/usr/bin/env python3
"""
Analyze the Wikipedia PDF document structure to understand title and heading patterns.
"""

import fitz
import json
from collections import defaultdict

def analyze_document():
    doc = fitz.open('input/50 page sample PDF.indd.pdf')
    print(f'Total pages: {len(doc)}')
    
    # Analyze first few pages for title and structure
    for page_num in range(min(5, len(doc))):
        print(f'\n=== PAGE {page_num + 1} ===')
        page = doc[page_num]
        blocks = page.get_text('dict')['blocks']
        
        font_sizes = []
        text_items = []
        
        for block in blocks:
            if 'lines' in block:
                for line in block['lines']:
                    line_text = ''
                    line_spans = []
                    
                    for span in line['spans']:
                        line_text += span['text']
                        line_spans.append(span)
                    
                    line_text = line_text.strip()
                    if line_text and len(line_text) > 2:
                        if line_spans:
                            font_size = line_spans[0]['size']
                            is_bold = bool(line_spans[0]['flags'] & 2**4)
                            font_name = line_spans[0].get('font', '')
                            
                            font_sizes.append(font_size)
                            text_items.append({
                                'text': line_text,
                                'font_size': font_size,
                                'is_bold': is_bold,
                                'font_name': font_name,
                                'y_pos': line_spans[0]['bbox'][1]
                            })
        
        # Sort by font size (descending) and show largest fonts first
        text_items.sort(key=lambda x: x['font_size'], reverse=True)
        
        print(f"Font sizes found: {sorted(set(font_sizes), reverse=True)}")
        print("Largest text items:")
        for item in text_items[:10]:  # Show top 10 largest
            bold_marker = " [BOLD]" if item['is_bold'] else ""
            print(f"  {item['font_size']:.1f}pt{bold_marker}: {item['text'][:80]}...")
    
    # Look for title patterns across all pages
    print(f'\n=== TITLE SEARCH ACROSS ALL PAGES ===')
    title_candidates = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text('dict')['blocks']
        
        for block in blocks:
            if 'lines' in block:
                for line in block['lines']:
                    line_text = ''.join(span['text'] for span in line['spans']).strip()
                    
                    # Look for title-like patterns
                    if any(word in line_text.upper() for word in ['WIKIPEDIA', 'WORST', 'BEST', 'WRITING']):
                        if line['spans']:
                            font_size = line['spans'][0]['size']
                            is_bold = bool(line['spans'][0]['flags'] & 2**4)
                            title_candidates.append({
                                'page': page_num + 1,
                                'text': line_text,
                                'font_size': font_size,
                                'is_bold': is_bold
                            })
    
    print("Title candidates found:")
    for candidate in title_candidates:
        bold_marker = " [BOLD]" if candidate['is_bold'] else ""
        print(f"  Page {candidate['page']}: {candidate['font_size']:.1f}pt{bold_marker}: {candidate['text']}")
    
    doc.close()

if __name__ == '__main__':
    analyze_document()
