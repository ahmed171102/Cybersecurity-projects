# 33 — Blue team lab

## What this is

A topology of three machines on an isolated lab network, and one detection: 5 failed SSH logins in 5 minutes.

## Why it matters

A detection without a place to see the logs is a sentence. The monitor VM is the place.

## How to run

Open `topology.mmd` and read `DETECTION.md`. Build the three VMs only on a host-only network.

## Portfolio deliverable

A screenshot of the diagram and five log lines from your own lab that match the use case.

## Exercise

Add the monitor VM's IP to topology.mmd. Write five Failed password lines that would match the 5-in-5-minutes use case.

