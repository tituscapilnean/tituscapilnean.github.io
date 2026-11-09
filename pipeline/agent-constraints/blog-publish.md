# Publishing

The `publishing` stage already wrote `_posts/<date>-<slug>.md` and removed the draft. Open the pull request:

1. In the blog repo: `git switch main && git pull --ff-only && git switch -c post/<slug>`. The untracked post comes along.
2. Stage only the post: `git add _posts/<date>-<slug>.md`. Check `git diff --cached --name-only` lists exactly that file. Never commit unrelated changes Titus has in the working tree (like `.gitignore` or `.DS_Store`).
3. Commit `feat: add post: <title>` with the attribution line from the session.
4. Push, and open a PR against main with a short body: the date, the argument in one or two lines, how it was made (interview, voice review, fact check), and the PR attribution line.
5. Wait for the PR Check workflow. Record its result with the PR.
6. Never merge. Titus merges.
