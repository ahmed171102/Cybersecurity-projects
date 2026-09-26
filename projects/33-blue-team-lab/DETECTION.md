# Detection use case

Network: isolated lab only. The attacker VM, the target, and the monitor share that network and nothing else.

Use case: 5 failed SSH logins in 5 minutes against the target.

What the monitor should see: five `Failed password` lines, same source, inside five minutes.

What you do: alert, then ask whether that source is the attacker VM you planned for this exercise. If it is not on the lab diagram, stop and disconnect the VM.

What you do not do: scan anything outside the isolated network.
