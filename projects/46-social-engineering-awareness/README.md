# 46 — Social engineering awareness

## What this is

An interactive quiz with three questions: an urgent link, a fake IT password call, and a found USB. Defensive only. Nothing is stored.

## Why it matters

Most account theft starts with a person, not with a scanner. The habit is: do not use the surprise channel.

## How to run

```bash
python3 projects/46-social-engineering-awareness/quiz.py --demo
python3 projects/46-social-engineering-awareness/quiz.py
```

`--demo` prints the safer answers so the smoke test and a hurried review can read them.

## Portfolio deliverable

Your score and one extra question you wrote about a fake delivery SMS.

## Exercise

Add a fourth question: a calendar invite from outside the company that asks you to enable a macro. Safer answer: decline and ask the person on a channel you already use.
