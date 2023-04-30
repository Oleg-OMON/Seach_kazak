import pytest
from sqlalchemy import insert, select
from conftest import client, async_session_maker


def test_register():
    assert  1 == 1