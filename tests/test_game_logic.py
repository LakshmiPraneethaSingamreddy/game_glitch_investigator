from pathlib import Path
import sys

# Allow running this file directly from different working directories.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess
from logic_utils import build_new_game_state, should_reset_for_difficulty_change

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_one_above_secret_is_too_high():
    # Edge case: nearest value above secret should still show lower hint
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_one_below_secret_is_too_low():
    # Edge case: nearest value below secret should still show higher hint
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_new_game_state_resets_round_values_but_keeps_score():
    state = build_new_game_state(
        low=1,
        high=100,
        randint_func=lambda _low, _high: 42,
        current_score=35,
    )

    assert state["secret"] == 42
    assert state["attempts"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    assert state["score"] == 35


def test_new_game_state_uses_given_range_for_secret_generation():
    captured = {}

    def fake_randint(low, high):
        captured["low"] = low
        captured["high"] = high
        return 7

    state = build_new_game_state(
        low=5,
        high=10,
        randint_func=fake_randint,
        current_score=0,
    )

    assert captured == {"low": 5, "high": 10}
    assert state["secret"] == 7


def test_should_reset_for_difficulty_change_only_when_difficulty_differs():
    assert should_reset_for_difficulty_change("Normal", "Hard") is True
    assert should_reset_for_difficulty_change("Easy", "Easy") is False
