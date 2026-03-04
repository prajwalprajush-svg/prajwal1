"""Tests for the Flask web interface."""

import pytest

from cgpa_calculator.web import app


def test_index_get():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'CGPA Calculator' in response.data


def test_index_post_valid():
    client = app.test_client()
    data = {'courses': 'A 3\nB+ 4'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Result:' in response.data
    assert b'8.43' in response.data


def test_index_post_invalid():
    client = app.test_client()
    data = {'courses': 'A three'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Error:' in response.data
