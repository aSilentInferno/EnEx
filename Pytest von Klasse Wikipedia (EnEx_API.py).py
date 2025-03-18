import pytest
import json
from unittest.mock import patch, MagicMock
from EnEx_API.py import get_wiki_page, get_inbound_links, get_outbound_links, get_wiki_links

def test_get_wiki_page():
    """Testet, ob get_wiki_page eine Wikipedia-Instanz zurückgibt."""
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.text = "<html>Mocked Wikipedia Page</html>"
        wiki_page = get_wiki_page("Python")
        assert wiki_page.name == "Python"
        assert "Mocked Wikipedia Page" in wiki_page.inhalt

def test_get_inbound_links():
    """Testet, ob get_inbound_links eine gültige JSON-Antwort zurückgibt."""
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.json = MagicMock(return_value={"query": {"backlinks": [{"title": "Test"}]}})
        response = get_inbound_links("Python")
        assert "query" in response
        assert "backlinks" in response["query"]

def test_get_outbound_links():
    """Testet, ob get_outbound_links eine gültige JSON-Antwort zurückgibt."""
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.json = MagicMock(return_value={"query": {"pages": {"123": {"links": [{"title": "Test"}]}}}})
        response = get_outbound_links("Python")
        assert "query" in response
        assert "pages" in response["query"]

def test_get_wiki_links():
    """Testet, ob get_wiki_links eine Wikipedia-Instanz mit Links zurückgibt."""
    with patch("requests.get") as mocked_get:
        mocked_get.side_effect = [
            MagicMock(json=MagicMock(return_value={"query": {"backlinks": [{"title": "Test Inbound"}]}})),
            MagicMock(json=MagicMock(return_value={"query": {"pages": {"123": {"links": [{"title": "Test Outbound"}]}}}}))
        ]
        wiki = get_wiki_links("Python")
        assert "Test Inbound" in json.dumps(wiki.inbound_links)
        assert "Test Outbound" in json.dumps(wiki.outbound_links)

if __name__ == "__main__":
    pytest.main()
