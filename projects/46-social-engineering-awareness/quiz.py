"""Three defensive questions. Educational only. No password collection."""

from __future__ import annotations

import sys

QUESTIONS = [
    {
        "prompt": "A message says your mailbox closes in 10 minutes and includes a link. What do you do?",
        "options": {"a": "Open the link and sign in", "b": "Ignore the link and open the official app"},
        "answer": "b",
        "why": "Urgency plus a link is the pattern. The official app is the one you already installed.",
    },
    {
        "prompt": "Someone on the phone says they are IT and need your password to fix email. What do you do?",
        "options": {"a": "Read the password so they can help", "b": "Hang up and call the number in the staff directory"},
        "answer": "b",
        "why": "IT already has admin tools. They do not need your password. Call a number you already have.",
    },
    {
        "prompt": "You find a USB stick in the parking lot labeled payroll. What do you do?",
        "options": {"a": "Plug it into your work laptop to see whose it is", "b": "Leave it at reception or give it to security unopened"},
        "answer": "b",
        "why": "A found USB is a common way to run unexpected software. Do not plug it into a machine you care about.",
    },
]


def ask() -> None:
    score = 0
    for index, item in enumerate(QUESTIONS, start=1):
        print(f"\n{index}. {item['prompt']}")
        for key, text in item["options"].items():
            print(f"   {key}) {text}")
        choice = input("answer> ").strip().lower()
        if choice == item["answer"]:
            score += 1
            print("correct")
        else:
            print("not the safer habit")
        print(item["why"])
    print(f"\n{score}/{len(QUESTIONS)}")


def demo() -> None:
    print("Demo answers. Run without --demo to take the quiz.\n")
    for index, item in enumerate(QUESTIONS, start=1):
        print(f"{index}. {item['prompt']}")
        print(f"   safer: {item['answer']}) {item['options'][item['answer']]}")
        print(f"   {item['why']}\n")


def main() -> None:
    if "--demo" in sys.argv:
        demo()
        return
    ask()


if __name__ == "__main__":
    main()
