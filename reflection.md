# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
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
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
