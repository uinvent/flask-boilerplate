def test_get_persons(client):
    rs = client.get("/person/")

    assert rs.status_code == 200
    all_persons = rs.json
    assert len(all_persons) > 0

    selected_person = all_persons[0]
    rs = client.get("/person/" + str(selected_person['id']))

    assert rs.status_code == 200
    person = rs.json
    assert person is not None
    assert person['id'] == selected_person['id']


def test_get_all_address(client):
    all_persons = client.get("/person/").json
    selected_person = all_persons[0]
    rs = client.get("/person/" + str(selected_person['id']) + "/address/")
    assert rs.status_code == 200

