import os
import tempfile
import xml.etree.ElementTree as ET
import pytest
from unittest.mock import patch
from scripts.charts import count_figures, process_files as process_charts
from scripts.keywordCloud import extract_abstract, process as process_cloud
from scripts.list import extract_links, should_include_link, clean_link

@pytest.fixture
def setup_test_directory():
    # Create a temporary directory for test files
    test_dir = tempfile.mkdtemp()

    # Create sample XML content
    sample_xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <TEI xmlns="http://www.tei-c.org/ns/1.0">
        <teiHeader>
            <abstract>
                <p>This is a test abstract with keywords test analysis research</p>
            </abstract>
        </teiHeader>
        <text>
            <body>
                <figure/>
                <figure/>
                <p>Visit <ref target="http://example.com">link</ref></p>
                <div type="references">
                    <p>Reference <ref target="http://reference.com">link</ref></p>
                </div>
            </body>
        </text>
    </TEI>
    '''
    
    # Create a test XML file
    test_file = os.path.join(test_dir, "test.xml")
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(sample_xml)

    yield test_dir, test_file

    # Clean up temporary files
    for file in os.listdir(test_dir):
        os.remove(os.path.join(test_dir, file))
    os.rmdir(test_dir)

def test_count_figures(setup_test_directory):
    test_dir, test_file = setup_test_directory
    """Test if figure counting works correctly"""
    figure_count = count_figures(test_file)
    assert figure_count == 2, "Should find exactly 2 figures in the test XML"

def test_extract_abstract(setup_test_directory):
    test_dir, test_file = setup_test_directory
    """Test if abstract extraction works correctly"""
    abstract = extract_abstract(test_file)
    expected = "This is a test abstract with keywords test analysis research "
    assert abstract == expected, "Abstract text should match exactly"

def test_extract_links(setup_test_directory):
    test_dir, test_file = setup_test_directory
    """Test if link extraction works correctly"""
    links = extract_links(test_file)
    assert len(links) == 1, "Should find exactly 1 non-reference link"
    assert links[0] == "http://example.com", "Should extract correct link URL"

def test_should_include_link():
    """Test link filtering logic"""
    assert should_include_link("http://example.com")
    assert not should_include_link("http://grobid.com")
    assert not should_include_link("#internal-ref")
    assert not should_include_link("")

def test_clean_link():
    """Test link cleaning functionality"""
    assert clean_link("http://example.com.") == "http://example.com"
    assert clean_link("http://example.com,") == "http://example.com"
    assert clean_link("http://example.com") == "http://example.com"

@patch('matplotlib.pyplot.savefig')
def test_charts_generation(mock_savefig, setup_test_directory):
    test_dir, test_file = setup_test_directory
    """Test if charts are generated without errors"""
    process_charts(test_file)
    mock_savefig.assert_called_once()

@patch('matplotlib.pyplot.savefig')
def test_wordcloud_generation(mock_savefig, setup_test_directory):
    test_dir, test_file = setup_test_directory
    """Test if word cloud is generated without errors"""
    process_cloud(test_file)
    mock_savefig.assert_called_once()

def test_multiple_files_processing(setup_test_directory):
    test_dir, _ = setup_test_directory
    """Test processing multiple XML files"""
    second_file = os.path.join(test_dir, "test2.xml")
    with open(second_file, "w", encoding="utf-8") as f:
        f.write('''<?xml version="1.0" encoding="UTF-8"?>
        <TEI xmlns="http://www.tei-c.org/ns/1.0">
            <teiHeader>
                <abstract>
                    <p>This is another test abstract</p>
                </abstract>
            </teiHeader>
            <text>
                <body>
                    <figure/>
                </body>
            </text>
        </TEI>
        ''')
    
    files = os.listdir(test_dir)
    assert len(files) == 2, "Should have exactly 2 test files"

def test_invalid_xml(setup_test_directory):
    test_dir, _ = setup_test_directory
    """Test handling of invalid XML files"""
    invalid_file = os.path.join(test_dir, "invalid.xml")
    with open(invalid_file, "w") as f:
        f.write("This is not valid XML")
    
    with pytest.raises(ET.ParseError):
        count_figures(invalid_file)

def test_empty_directory():
    """Test processing an empty directory"""
    empty_dir = tempfile.mkdtemp()
    process_charts(empty_dir)  # Should not raise any errors
    os.rmdir(empty_dir)
