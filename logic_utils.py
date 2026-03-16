def get_range_for_difficulty(difficulty: str):
    #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def should_reset_for_difficulty_change(last_difficulty: str, current_difficulty: str):
    #FIX: Added logic into logic_utils.py so that the game restarts when difficulty is changed using Copilot Agent mode
    """Return True when game state should reset after a difficulty change."""
    return last_difficulty != current_difficulty


def build_new_game_state(low: int, high: int, randint_func, current_score: int):
     #FIX: Added build_new_game logic into logic_utils.py so that it creates a new game when user presses on the new_game button using Copilot Agent mode
    """Return the session-state values for starting a fresh round."""
    return {
        "attempts": 0,
        "secret": randint_func(low, high),
        "status": "playing",
        "history": [],
        "score": current_score,
    }


def parse_guess(raw: str):
    #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
