# import pytest
# from tests.fixtures import api_client
#
#
# @pytest.mark.djago_db
# def test_user(api_client):
#     response = api_client.post(
#         "user/",
#         json={
#             "username": "test",
#             "password": "test123"
#         }
#     )
#     assert response.status_code == 200
