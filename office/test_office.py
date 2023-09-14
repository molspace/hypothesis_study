from typing import Callable
import pytest
from hypothesis import given, settings
from hypothesis.strategies import integers, composite, SearchStrategy

from office import Employee, fire_random_employee, generate_random_team

@composite
def teams(draw: Callable[[SearchStrategy[int]], int], min_value: int = 1, max_value: int = 20):
	rand_val = draw(integers(min_value, max_value))
	return generate_random_team(rand_val)

@given(integers(max_value=0))
def test_negative_team_size(team_size: int):
	with pytest.raises(ValueError):
		generate_random_team(team_size)

@given(integers(1,20))
def test_team_size(team_size: int):
	team = generate_random_team(team_size)
	assert len(team) == team_size

@given(teams())
def test_team_has_ceo(team):
	assert Employee.CEO in team

@given(teams())
def test_fire_employee(team):
	team_copy = team.copy()
	fire_random_employee(team_copy)
	assert len(team_copy) == len(team) - 1