# Voice interview

The interview is how the post gets Titus's real moments, numbers and opinions. Each question is asked through the browser recorder:

    swamp behavior run blog-pipeline ask --input slug=<workItem> --input "question=<question>"

Run it in the background, tell Titus the question is open in his browser, and wait for the completion notice. Then read the answer:

    swamp data query 'behavior("blog-pipeline") && name.startsWith("qa-")' --select content --json | jq '.results | sort_by(.answeredAt) | last'

Rules:
- One question at a time. Write the next question after reading the last answer, so it follows up on what he actually said.
- Four questions is the usual arc:
  1. **The moment:** take him to the scene that made him want to write this.
  2. **The hard or subtle part:** where the obvious version of the argument breaks, or where he is part of the problem. This is where the self-admission usually comes from.
  3. **A concrete example:** one real process, company or campaign, with what it cost.
  4. **The fix and the bar:** what he would change, and what would have to be true for it to work.
- Ask one more if an answer opens something big. Stop at five.
- After each answer, tell him in a few lines what you took from it, quoting his strongest line. Don't paraphrase his words into stronger claims.
- Transcripts are speech-to-text. Flag words that look misheard and ask before using them.
- After the interview, list what's still missing (opening detail, numbers, a real run) and ask for those in chat.
