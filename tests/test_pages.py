def test_runs_page_shows_empty_message(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"No runs yet" in response.data