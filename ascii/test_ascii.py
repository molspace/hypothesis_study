from ascii import from_ascii_code, to_ascii_code
from hypothesis import given, example, settings
from hypothesis.strategies import text


@given(text())
@example("")
@settings(max_examples=100)
def test_decode_intverts_encode(test_str: str) -> None:
	assert from_ascii_code(to_ascii_code(test_str)) == test_str


@given(text())
def test_list_length_same_as_input_str(test_str: str) -> None:
	encoded = to_ascii_code(test_str)
	assert len(encoded) == len(test_str)
