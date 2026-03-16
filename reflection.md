# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran think it felt quite right but way too wrong. Like everything works but not in the way it should be(Incorrectly).
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1) The first bug i have observed is that the hints are always "Go lower" no matter my guess is either big or smaller than the secret number. 
2) The second bug that i have identified is once if i guess the correct number and then if i want to play again, it is starting the new game but it is not letting me submit the number basically the start game button is not working properly.
3) The third bug is the secret number is not chosen according to the difficulty levels. It is chosen randomly from 1-100 without considering those levels.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I have used the Copilot in this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Intially in the given code, the secret is converted into string for the even numbered guesses which in turn making the hints backwards. The copliot identified that and when I changed the code according to the copilot's suggestion, it worked.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
So when i was trying to fix the start_new_game bug which is starting a new game, but it is not allowing me to submit my guess. The copliot made the changes, but it also resetted the score to '0'(which is useful if i want to start a new game entirely). But if i want to continue playing after guessing the number correct, the score should be carried forward to the next level. In this case the copilot made a minor mistake for not considering this case.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Everytime, I finish modifying the code for resolving the bug I will check for all the possible tests cases I can think of and I will test manually in the website. And then I will write some tests with help of AI and I will run tests using the pytest.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
When resolving the new_game creation bug I have modified the code and then I tested it manually in the website where I have identified that the modified code is resetting the score to zero everytime, so I have modified in such a way that it retains score from the previous games and then checked again. And then I also wrote some tests using teh github copilot and then ran those tests,all passed.
- Did AI help you design or understand any tests? How?
I have used github copilot for writing the tests for all the bugs I have resolved. It gave me the tests and also explanations fir why it gave those tests. It helped me understand why certain tests are necessary like the edge case tests and what happens if we miss such tests and how our system might fail in some critical times( for high priority apps).

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
In the original app the secret number kept changing because every time we interact with the streamlit it re runs the entire script which has the random secret generation number code. So, every time we interact with the app, it changed.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
So, Streamlit is like a whiteboard where every time you start to write on it, the whole board gets erased and redrawn from the beginning.
That means each click or input reruns the full script, so normal variables get recreated and can change, like the secret number in your game.
Session state works like a memory box that keeps important values safe between those redraws.
So even though the app keeps rerunning, your key data stays consistent.
- What change did you make that finally gave the game a stable secret number?
I modified the code, so that the secret number is generate only if the secret number is None in the current session or when the game restarts or when the difficulty level changes. Other than these 3 situations, the secret number remains same.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  The habit I want to reuse in the future lab is version control using git and also creating new branches for every bug that I have fixed.
- What is one thing you would do differently next time you work with AI on a coding task?
This time, I have used the same chat for every bug I have resolved , but from nect time, I want to use seperate chats for seperate bugs, so that it stays focused only on that bug at that points and I also want to improve my prompting.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It helped me to getter better at generating tests for the project and also to maintain clear ownership of how our code and the functionalty of the code should be so that we can create the app that we like. I feel sometimes we shouldn't blindly trust the suggestions from ai but overall I feel like using ai can help in making things faster.