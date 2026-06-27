import time
import random

print("===== Typing Speed Tester =====")
print()
print("Type this sentence:")
print()

sentences = [
    "Python is a powerful programming language.",
    "Practice makes a person perfect.",
    "Coding improves problem solving skills!!!",
    "Consistency is the key to success."
]

original = random.choice(sentences)
print(original)

start = time.time()
typed = input("Your Input: ")
end = time.time()

time_taken = end - start

words = len(typed.split())

if time_taken > 0:
    wpm = (words / time_taken) * 60
else:
    wpm = 0

original_words = original.split()
typed_words = typed.split()

correct = 0

for i in range(min(len(original_words), len(typed_words))):
    if original_words[i] == typed_words[i]:
        correct += 1

accuracy = (correct / len(original_words)) * 100

with open("test_score.txt", "a") as file:
    file.write(
        f"Sentence: {original} | WPM: {round(wpm, 2)} | Accuracy: {round(accuracy, 2)}%\n"
    )

print("Score saved to test_score.txt")

print("\nTime Taken:", round(time_taken, 2), "seconds")
print("WPM:", round(wpm, 2))
print("Accuracy:", round(accuracy, 2), "%")

if accuracy >= 90:
    print("Excellent Typing!")
elif accuracy >= 70:
    print("Good Typing!")
else:
    print("Needs Practice!")
