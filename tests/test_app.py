from playwright.sync_api import Page, expect
from datetime import datetime

def test_get_peeps(page, web_client, db_connection):
    db_connection.execute(
        'INSERT INTO peeps (author, peep, time_posted) VALUES (%s, %s, %s)',
        ['test author_1', 'this is a test peep', datetime(2025, 1, 15, 15, 17, 0)]
    )
    
    response = web_client.get('/home')
    html = response.data.decode()

    assert response.status_code == 200
    assert 'class="peep-author"' in html
    assert 'class="peep-content"' in html
    assert 'class="peep-timestamp"' in html

    
