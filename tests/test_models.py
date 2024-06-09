def test_word_model():
    """
    Test the Word model
    """
    from app.models import Word
    word = Word(text="example")
    assert word.text == "example"
    assert word.pronunciations == []
    assert word.translations == []
