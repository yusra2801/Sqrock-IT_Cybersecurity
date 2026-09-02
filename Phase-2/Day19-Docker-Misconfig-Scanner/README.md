### Day 19 — Docker Container Misconfiguration Scanner

Container configuration determines its operational privileges. Running a container as root (no explicit `USER` instruction), using an unpinned `:latest` base image (which can pull unpredictable/unstable versions), or exposing the SSH port (22) are all serious security risks that can lead to host breakout or unauthorized access. In this task, I wrote a static analyzer that parses a Dockerfile line by line to detect these three misconfigurations. Running it against a test Dockerfile detected all three issues: `FROM ubuntu:latest` (unpinned tag), `EXPOSE 22` (SSH port exposed), and no `USER` instruction present (implicit root execution).

**Secure Dockerfile checklist:**
- Use a specific version tag (e.g. `ubuntu:22.04`) instead of `:latest`
- Always include an explicit `USER` instruction with a non-root user
- Only expose ports that are actually needed — never expose SSH (22) in production containers
- Use multi-stage builds so build tools and secrets don't end up in the final image