from typing import Callable
import pytest
from hypothesis import given, settings
from hypothesis.strategies import integers

from office import Employee, fire_random_employee, generate_random_team


@given(integers(max_value=0))
def test_negative_team_size(team_size: int):
	with pytest.raises(ValueError):
		generate_random_team(team_size)

@given(integers(min_value=1, max_value=20))
def test_team_size(team_size: int):
	assert len(generate_random_team(team_size)) == team_size

@given(integers(min_value=1, max_value=20))
def test_team_has_ceo(team_size: int):
	team = generate_random_team(team_size)
	assert Employee.CEO in team

@given(integers(min_value=1, max_value=20))
