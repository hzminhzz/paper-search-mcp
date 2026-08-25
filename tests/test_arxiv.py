# tests/test_arxiv.py
import os
import tempfile
import unittest
from unittest.mock import Mock

from paper_search_mcp.academic_platforms.arxiv import ArxivSearcher

class TestArxivSearcher(unittest.TestCase):
    def test_search(self):
        searcher = ArxivSearcher()
        papers = searcher.search("machine learning", max_results=10)
        print(f"Found {len(papers)} papers for query 'machine learning':")
        for i, paper in enumerate(papers, 1):
            print(f"{i}. {paper.title} (ID: {paper.paper_id})")
        if not papers:
            self.skipTest("arXiv API is unavailable or rate-limited")
        self.assertEqual(len(papers), 10)
        self.assertTrue(papers[0].title)

    def test_download_rejects_non_pdf_response(self):
        searcher = ArxivSearcher()
        response = Mock()
        response.headers = {"content-type": "text/html; charset=utf-8"}
        response.content = b"<html>not a paper</html>"
        response.raise_for_status.return_value = None
        searcher.session.get = Mock(return_value=response)

        with tempfile.TemporaryDirectory() as save_path:
            with self.assertRaisesRegex(ValueError, "was not a PDF"):
                searcher.download_pdf("INVALID_IDENTIFIER", save_path)
            self.assertEqual(os.listdir(save_path), [])

if __name__ == '__main__':
    unittest.main()