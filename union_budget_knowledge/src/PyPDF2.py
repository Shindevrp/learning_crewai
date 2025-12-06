# Minimal stub for PyPDF2 to allow project to run without full package install
# (disk space constraints)

class PdfReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pages = []
    
    def __getitem__(self, index):
        return {"extract_text": lambda: "Mock PDF page text"}

__all__ = ["PdfReader"]
