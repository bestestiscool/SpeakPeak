def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to SpeakPeak Dictionary" in response.data

def test_search_word(test_client):
    response = test_client.post('/words/search', data={'word': 'example'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Results for \"Example\"" in response.data

def test_results_page(test_client):
    response = test_client.get('/words/results/example')
    assert response.status_code == 200
    assert b"Results for \"Example\"" in response.data
